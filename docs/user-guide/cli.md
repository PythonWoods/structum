# CLI Usage

The main command is `structum`.

## Arguments

*   `DIRECTORY`: The root directory to analyze. Defaults to current directory (`.`).

## Options

### Filtering

*   `--ext, -e`: Filter by extension. Can be used multiple times.
    *   Example: `structum . -e py -e md` (Shows only Python and Markdown files).
*   `--ignore, -i`: Ignore specific directory names.
    *   Example: `structum . -i .git -i build`
*   `--hidden / --no-hidden`: Show or hide dotfiles (files starting with `.`). Default is hidden.
*   `--no-empty`: Hides directories that don't contain any visible files (useful when aggressive filtering is applied).

### Display

*   `--depth, -d`: Limit the traversal depth. Useful for large projects.
    *   Example: `structum . -d 2`
*   `--theme, -t`: Choose the visual theme (`emoji`, `nerd`, `ascii`, `none`).