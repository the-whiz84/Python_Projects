# Day 98 - Practical Python Automation Workflows

Day 98 now has a concrete automation script: `rename_extensions.py`. It walks a directory tree, normalizes file extensions, optionally remaps one extension to another, and does it in a way that is safer for Syncthing-synced folders than a naive rename loop.

That makes this project a good example of practical automation: repetitive, easy to get wrong by hand, and worth making predictable.

## 1. Start With a Real Workflow Worth Automating

The script targets a common file-maintenance job: fixing inconsistent extensions across a directory tree.

That sounds small, but it becomes painful fast when:

- files were created on different operating systems
- extensions differ only by case, such as `.JPG` versus `.jpg`
- you need to remap one extension to another, such as `.mdc` to `.md`
- the directory is synced by Syncthing and case-only renames can behave badly across devices

This is exactly the kind of workflow automation is good at. The rules are clear, the task is repetitive, and manual renaming is easy to mess up.

## 2. Keep the Rename Logic Separate From the CLI

The script is organized around a small set of focused helpers:

- `should_skip_file()` ignores hidden files and Syncthing metadata patterns
- `compute_new_extension()` decides what the new extension should be
- `safe_rename()` performs the actual rename, including case-only-safe handling
- `rename_extensions()` walks the directory tree and applies the rule set

That keeps the main automation logic reusable instead of burying everything inside argument parsing.

The extension computation is the center of the workflow:

```python
def compute_new_extension(
    ext: str,
    from_ext: Optional[str],
    to_ext: Optional[str],
    lowercase: bool,
) -> str:
    original_ext = ext

    if from_ext:
        from_ext = from_ext if from_ext.startswith(".") else f".{from_ext}"
        from_ext = from_ext.lower()
    if to_ext:
        to_ext = to_ext if to_ext.startswith(".") else f".{to_ext}"

    if lowercase:
        ext = ext.lower()

    if from_ext and original_ext.lower() == from_ext:
        if to_ext:
            ext = to_ext

    return ext
```

That gives the script two useful modes:

- lowercase all extensions by default
- explicitly remap one extension to another when requested

## 3. Make the Rename Safe for Syncthing-Style Environments

The most important part of the script is not the directory walk. It is the safe rename behavior.

```python
def safe_rename(old_path: str, new_path: str, dry_run: bool = False) -> None:
    if dry_run:
        print(f"[DRY RUN] Would rename: {old_path} -> {new_path}")
        return

    if os.path.exists(new_path) and old_path.lower() != new_path.lower():
        print(
            f"Skipping {os.path.basename(old_path)} -> {os.path.basename(new_path)}: "
            f"target already exists and is a different file"
        )
        return

    temp_path = old_path + ".renaming_temp"
    os.rename(old_path, temp_path)
    os.rename(temp_path, new_path)
```

That temporary rename step matters. Case-only renames can be inconsistent across filesystems and sync tools. Renaming through an intermediate temp name reduces that risk.

The script also skips Syncthing metadata and hidden files:

```python
SYNCTHING_META_DIRS = {".stfolder", ".stversions"}
SYNCTHING_META_PATTERNS = ("~syncthing~", ".syncthing.", ".stignore")
```

That is what makes this more than a generic renamer. It is written for a real sync environment where touching the wrong files can cause churn or conflicts.

## 4. Expose the Automation Through a Clear CLI

The script uses `argparse` to make the workflow usable from the shell:

```python
parser.add_argument("root", nargs="?", default=".")
parser.add_argument("--from-ext", dest="from_ext", default=None)
parser.add_argument("--to-ext", dest="to_ext", default=None)
parser.add_argument("--no-lowercase", dest="lowercase", action="store_false")
parser.add_argument("--dry-run", action="store_true")
```

That gives the automation a few practical use cases:

- lowercase every extension in a project:
  ```bash
  python rename_extensions.py /path/to/project --dry-run
  ```
- remap one extension type:
  ```bash
  python rename_extensions.py /path/to/project --from-ext .mdc --to-ext .md
  ```
- preview changes safely before touching any files:
  ```bash
  python rename_extensions.py . --dry-run
  ```

The `--dry-run` option is especially important. For bulk file operations, preview mode is one of the best safeguards you can add.

## How to Run the Automation

1. Change into the Day 98 project folder or point the script at any target directory.
2. Preview changes first:
   ```bash
   python rename_extensions.py . --dry-run
   ```
3. Run the real rename once the preview looks correct:
   ```bash
   python rename_extensions.py .
   ```
4. Use explicit remapping when needed:
   ```bash
   python rename_extensions.py . --from-ext .mdc --to-ext .md
   ```

## Summary

Day 98 now demonstrates what a practical automation script looks like in the real world. `rename_extensions.py` takes a repetitive filesystem task, encodes the rules explicitly, skips Syncthing metadata, handles case-only renames safely, and exposes the whole workflow through a CLI with a dry-run mode. That is the real point of automation: take a job that is boring and fragile by hand, then make it safe, repeatable, and easy to reuse.
