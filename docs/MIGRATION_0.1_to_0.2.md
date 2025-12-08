# Migration Guide: v0.1 to v0.2

**Date:** 2025-12-08
**Severity:** 🟢 INTERNAL REFACTORING
**User Impact:** None (no external plugins exist yet)

---

## Overview

Version 0.2 introduces a **major refactoring of the plugin system** to simplify architecture and prepare for future official plugins (like `structum-latex` and `structum-ai`).

**Good News**: Since no external plugins have been published yet, this is a **breaking change for internal development only**. End users are **not affected**.

### What Changed (Internal)

- ❌ **Removed**: Built-in plugins (filesystem scanning)
- ❌ **Removed**: `.dev` marker system
- ❌ **Removed**: `--show-dev` CLI flag
- ✅ **Added**: Official plugin detection (`structum_*`)
- ✅ **Added**: Plugin type tracking (OFFICIAL/EXTERNAL)
- ✅ **Enhanced**: Conflict detection and warnings

---

## Breaking Changes

### 1. Built-in Plugins Removed

**Before (v0.1):**
```
structum/
└── src/structum/plugins/
    ├── sample/          # Built-in plugin
    └── my_plugin/       # Built-in plugin
```

**After (v0.2):**
```
structum/
└── src/structum/plugins/
    └── [system files only, no plugins]
```

**Impact**: If you had built-in plugins in the Structum repository, they must be converted to external plugins.

---

### 2. .dev Marker System Removed

**Before (v0.1):**
```bash
structum plugins new my-plugin
# Creates plugin with .dev marker

structum plugins list --show-dev
# Shows dev-mode plugins

rm my_plugin/.dev
# Promotes to production
```

**After (v0.2):**
```bash
structum plugins new my-plugin
# Creates plugin WITHOUT .dev marker

structum plugins list
# Shows all installed plugins

# No dev mode - use version control for WIP
```

**Impact**: `.dev` marker files are ignored. Use your version control system (git branches) for work-in-progress plugins.

---

### 3. --show-dev Flag Removed

**Before (v0.1):**
```bash
structum plugins list --show-dev
```

**After (v0.2):**
```bash
structum plugins list
# Shows all installed plugins with type tags
```

**Impact**: The `--show-dev` flag no longer exists. All plugins are shown by default.

---

### 4. Official vs External Plugin Distinction

**New in v0.2:**

Plugins are now automatically categorized:

- **[OFFICIAL]**: Package name starts with `structum_*`
- **[EXTERNAL]**: All other plugins

```bash
$ structum plugins list

┌─────────────┬──────────────┬─────────┬─────────┬─────────────┐
│ Name        │ Type         │ Version │ Status  │ Description │
├─────────────┼──────────────┼─────────┼─────────┼─────────────┤
│ latex       │ [OFFICIAL]   │ 1.0.0   │ enabled │ LaTeX export│
│ my-plugin   │ [EXTERNAL]   │ 0.1.0   │ enabled │ My plugin   │
└─────────────┴──────────────┴─────────┴─────────┴─────────────┘
```

---

## Migration Steps

### For End Users

**No action required!**

Since no external plugins have been published yet, end users are completely unaffected. Core commands (`tree`, `docs`, `archive`, etc.) work identically.

---

### For Future Plugin Developers

When creating plugins in v0.2, use the new simplified workflow:

1. **Generate Skeleton**
   ```bash
   structum plugins new my-plugin
   ```

2. **Create Package Structure**
   Follow the generated structure and add `pyproject.toml`

3. **Add Entry Point**
   ```toml
   [project.entry-points."structum.plugins"]
   my-plugin = "my_plugin:MyPluginPlugin"
   ```

4. **Install and Test**
   ```bash
   pip install -e .
   structum plugins list  # Verify it appears
   ```

No `.dev` markers, no filesystem scanning - just standard Python packaging!

---

### For Structum Contributors

If you were developing built-in plugins in the Structum repository:

1. **Convert to external plugin** using steps above
2. Remove from `src/structum/plugins/` directory
3. Create separate repository for the plugin
4. Publish to PyPI when ready

See `docs/development/plugins.md` for complete guide.

---

## FAQ

### Q: Will my external plugins break?

**A:** No. External plugins using entry points work unchanged.

---

### Q: What happened to the sample plugin?

**A:** The sample plugin was removed as it's no longer needed. The skeleton generator creates fully-featured plugin templates.

---

### Q: Can I still create plugins?

**A:** Yes! Use `structum plugins new <name>` to generate a plugin skeleton, then install it as an external plugin.

---

### Q: How do I create an "official" plugin?

**A:** Official plugins are maintained by the PythonWoods team. External developers create [EXTERNAL] plugins.

To make your package name follow official convention (optional):
- Use `structum_<name>` as package name
- Your plugin will be auto-detected as [OFFICIAL]

---

### Q: What about plugin development workflow?

**A:** Use standard development practices:

1. Generate skeleton: `structum plugins new my-plugin`
2. Create git repository
3. Use branches for features
4. Install editable: `pip install -e .`
5. Test with `structum plugins list`

No special `.dev` marker needed - use version control!

---

### Q: Where can I find plugin examples?

**A:** Check the official plugins (when released):
- `structum-latex` - LaTeX export
- `structum-ai` - AI documentation generation

Or generate a new skeleton:
```bash
structum plugins new example-plugin
# Follow the instructions
```

---

## Deprecation Timeline

| Feature | Deprecated | Removed |
|---------|------------|---------|
| Built-in plugins | v0.2 | v0.2 |
| `.dev` marker | v0.2 | v0.2 |
| `--show-dev` flag | v0.2 | v0.2 |
| Filesystem scanning | v0.2 | v0.2 |

---

## Getting Help

- **Documentation**: https://github.com/pythonwoods/structum/docs
- **Issues**: https://github.com/pythonwoods/structum/issues
- **Migration Issues**: Tag with `migration-v0.2`

---

## Summary

**Benefits of v0.2:**
- ✅ Simpler architecture (-57% plugin loader code)
- ✅ No filesystem scanning
- ✅ Clear official vs external distinction
- ✅ Better conflict detection
- ✅ Consistent plugin loading mechanism

**Required Actions:**
- External plugin developers: No changes needed
- Built-in plugin developers: Convert to external plugins
- End users: No changes needed (unless plugins missing)

**Timeline:**
- v0.2 release: 2025-12-08
- Support for v0.1 plugin system: **Discontinued**
