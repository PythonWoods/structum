# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Code archiving functionality.

This module provides tools to traverse a codebase, collect source files based on
extensions, and generate Markdown archives. It supports features like Table of
Contents (ToC) generation and ASCII tree visualization.
"""

import os
from collections import defaultdict
from collections.abc import Sequence
from datetime import datetime
from pathlib import Path

from rich.console import Console

from structum_tree.core import get_tree_ascii
from structum_tree.utils import IGNORE_DIRS_DEFAULT, normalize_extensions

console = Console()


def gather_files(
    root: Path,
    extensions: Sequence[str] | None,
    ignore_dirs: Sequence[str] | None = None,
) -> list[tuple[Path, Path]]:
    """Collects all files matching the requested extensions.

    Recursively traverses the ``root`` directory, excluding directories specified
    in ``ignore_dirs`` (or defaults), and includes only files matching the
    provided extensions.

    Args:
        root: The root directory of the project.
        extensions: A sequence of file extensions to include (e.g., [".py", ".md"]).
            If None, ALL files (except ignored ones) will be collected.
        ignore_dirs: A sequence of directory names to exclude. If None, uses
            ``IGNORE_DIRS_DEFAULT``.

    Returns:
        A list of tuples ``(relative_path, absolute_path)`` for each collected file.
    """
    root = root.resolve()
    normalized_exts = normalize_extensions(extensions)

    ignored = set(ignore_dirs) if ignore_dirs else IGNORE_DIRS_DEFAULT
    collected: list[tuple[Path, Path]] = []

    for dirpath, dirnames, filenames in os.walk(root):
        # Filter directories in-place to prevent traversal
        dirnames[:] = [d for d in dirnames if d not in ignored]
        current_dir = Path(dirpath)

        for filename in filenames:
            # If extensions is None or empty (after normalization checks), include all.
            # But normalize_extensions returns empty set for None.
            # We need to distinguish between "User provided explicit empty list" vs "User provided None"
            # However, normalize_extensions(None) -> set(). normalize_extensions([]) -> set().
            # So checking normalized_exts is not enough if we want default behaviors.
            # But wait, logic: if NO extensions specified, we usually want ALL files?
            # Or should we require at least one extension?
            # The bug report says "structum archive -o ~/draft" finds 0 files.
            # This implies default behavior should be "all files".
            
            should_include = False
            if not normalized_exts:
                 should_include = True
            elif any(filename.endswith(ext) for ext in normalized_exts):
                 should_include = True
            
            if should_include:
                full_path = current_dir / filename
                rel_path = full_path.relative_to(root)
                collected.append((rel_path, full_path))

    return collected


def write_markdown(
    path: Path,
    files: Sequence[tuple[Path, Path]],
    root: Path,
    toc: bool,
    include_tree: bool,
    verbose: bool,
    extensions: Sequence[str] | None = None,
    ignore_dirs: Sequence[str] | None = None,
) -> None:
    """Writes a Markdown archive containing the collected source files.

    Args:
        path: The path to the output Markdown file.
        files: A sequence of tuples ``(relative_path, absolute_path)``.
        root: The root directory of the project (used for relative paths).
        toc: If True, includes a Table of Contents.
        include_tree: If True, includes an ASCII directory tree.
        verbose: If True, prints status messages to the console.
        extensions: Extensions to filter the tree view.
        ignore_dirs: Directories to ignore in the tree view.
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    if verbose:
        console.print(f"✍️  Writing archive: [bold cyan]{path}[/bold cyan]")

    with path.open("w", encoding="utf-8") as md:
        md.write(f"# Code Archive for `{root.name}`\n\n")
        md.write(f"_Generated on {datetime.now().isoformat(timespec='seconds')}_\n\n")

        if include_tree:
            if verbose:
                console.print("   ➕ Including directory tree")
            md.write("## Project Structure\n\n")
            md.write("```text\n")
            # PASSING FILTERS TO TREE GENERATION
            # Use defaults if ignore_dirs is None, but get_tree_ascii handles None by default?
            # Actually get_tree_ascii treats ignore_dirs=None as "no specific ignores"? 
            # No, let's look at get_tree_ascii docstring in tree.py (it doesn't default to common ignores there).
            # But build_tree logic: excluded_dir_names = set(exclude_dirs or [])
            # So if we pass None, it filters nothing.
            # We want to match gather_files logic: ignore_dirs OR defaults.
            
            final_ignore_dirs = ignore_dirs if ignore_dirs is not None else IGNORE_DIRS_DEFAULT
            
            tree_str = get_tree_ascii(
                root, 
                extensions=extensions, 
                ignore_dirs=final_ignore_dirs
            )
            md.write(tree_str)
            md.write("\n```\n\n")

        if toc:
            if verbose:
                console.print("   ➕ Including Table of Contents")
            md.write("## Table of Contents\n\n")
            for rel_path, _ in files:
                anchor = str(rel_path).replace("/", "-").replace(".", "-")
                md.write(f"- [{rel_path}](#{anchor})\n")
            md.write("\n---\n\n")

        for rel_path, full_path in files:
            # Simple heuristic for code block language
            ext = full_path.suffix.replace(".", "") or "text"
            anchor = str(rel_path).replace("/", "-").replace(".", "-")

            md.write(f"## `{rel_path}` {{#{anchor}}}\n\n")
            md.write(f"```{ext}\n")
            try:
                content = full_path.read_text(encoding="utf-8", errors="replace")
                md.write(content)
            except Exception as exc:
                md.write(f"# ERROR reading file: {exc}")
            md.write("\n```\n\n")

    if verbose:
        console.print(f"✅ Archive created: [green]{path}[/green]")


def _create_archives_per_folder(
    root: Path,
    output_dir: Path,
    files: Sequence[tuple[Path, Path]],
    toc: bool,
    include_tree: bool,
    verbose: bool,
    extensions: Sequence[str] | None = None,
    ignore_dirs: Sequence[str] | None = None,
) -> None:
    """Generates a Markdown file for each directory containing collected files."""
    output_dir.mkdir(parents=True, exist_ok=True)
    grouped: defaultdict[Path, list[tuple[Path, Path]]] = defaultdict(list)

    for rel_path, full_path in files:
        grouped[rel_path.parent].append((rel_path, full_path))

    for folder, group_files in grouped.items():
        # Map '.' folder to 'root.md', others to 'path/to/dir.md'
        relative_dir = folder if folder != Path(".") else Path("root")
        out_path = output_dir / relative_dir.with_suffix(".md")
        write_markdown(out_path, group_files, root, toc, include_tree, verbose, extensions, ignore_dirs)


def _create_archives_per_type(
    root: Path,
    output_dir: Path,
    files: Sequence[tuple[Path, Path]],
    toc: bool,
    include_tree: bool,
    verbose: bool,
    extensions: Sequence[str] | None = None,
    ignore_dirs: Sequence[str] | None = None,
) -> None:
    """Generates a Markdown file for each file extension."""
    output_dir.mkdir(parents=True, exist_ok=True)
    grouped: defaultdict[str, list[tuple[Path, Path]]] = defaultdict(list)

    for rel_path, full_path in files:
        ext = full_path.suffix.replace(".", "") or "noext"
        grouped[ext].append((rel_path, full_path))

    for ext, group_files in grouped.items():
        out_path = output_dir / f"{ext}.md"
        write_markdown(out_path, group_files, root, toc, include_tree, verbose, extensions, ignore_dirs)


def create_archive(
    root: Path,
    output: Path,
    extensions: Sequence[str] | None,
    ignore_dirs: Sequence[str] | None = None,
    split_by_folder: bool = False,
    split_by_type: bool = False,
    toc: bool = True,
    include_tree: bool = True,
    verbose: bool = True,
) -> None:
    """Main entry point to create code archives.

    Args:
        root: Root directory of the project.
        output: Output file path (single mode) or directory path (split mode).
        extensions: List of file extensions to include.
        ignore_dirs: List of directory names to exclude.
        split_by_folder: If True, creates one archive per folder.
        split_by_type: If True, creates one archive per file extension.
        toc: If True, includes Table of Contents.
        include_tree: If True, includes directory tree.
        verbose: If True, enables verbose output.

    Raises:
        ValueError: If both split_by_folder and split_by_type are True.
    """
    if split_by_folder and split_by_type:
        raise ValueError("Cannot use both split_by_folder and split_by_type.")

    root = root.resolve()
    output = output.resolve()

    # FIX: Handle directory output for single file mode
    if output.is_dir() and not (split_by_folder or split_by_type):
        if verbose:
            console.print(f"[yellow]Address output '{output}' is a directory. Defaulting to '{output / 'archive.md'}'[/yellow]")
        output = output / "archive.md"

    files = gather_files(root, extensions, ignore_dirs)

    if verbose:
        console.print(f"📂 Project Root: [bold]{root}[/bold]")
        console.print(f"📄 Files found: [bold]{len(files)}[/bold]")

    if not files:
        if verbose:
            console.print("[yellow]No files found matching the criteria.[/yellow]")
        return

    if split_by_folder:
        if verbose:
            console.print("📁 Mode: Split by folder")
        _create_archives_per_folder(root, output, files, toc, include_tree, verbose, extensions, ignore_dirs)
        return

    if split_by_type:
        if verbose:
            console.print("📚 Mode: Split by extension")
        _create_archives_per_type(root, output, files, toc, include_tree, verbose, extensions, ignore_dirs)
        return

    # Single archive mode
    write_markdown(output, files, root, toc, include_tree, verbose, extensions, ignore_dirs)
