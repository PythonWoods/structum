# Custom Themes

While Structum comes with robust built-in themes (`emoji`, `nerd`, `ascii`), enterprise environments often require specific visual standards.

## How Themes Work

Internally, themes are defined as `IconSet` objects containing:
1.  **Folder Icons**: Open and closed states.
2.  **Default File Icon**: Fallback for unknown extensions.
3.  **Extension Map**: Dictionary mapping `.ext` to icons.
4.  **Filename Map**: Dictionary mapping specific filenames (e.g., `Dockerfile`) to icons.

## Creating a Custom Theme (Developer)

Currently, custom themes can be added by extending the `icons.py` module in the source code.

!!! note "Plugin System Coming Soon"
    In version `0.2.0`, we will introduce a YAML-based configuration to load custom themes without modifying the source code.

### Example: Minimalist Theme

If you wanted to create a "Minimalist" theme using simple geometric shapes:

```python
# In src/structum/core/icons.py

MINIMAL_SET = IconSet(
    folder_open="▼",
    folder_closed="▶",
    file_default="•",
    filenames={},
    extensions={
        ".py": "py",
        ".md": "md"
    }
)

# Add to THEMES registry
THEMES = {
    # ... existing themes ...
    "minimal": MINIMAL_SET
}
```

Once added, you can use it immediately via CLI:

```bash
structum . --theme minimal
```