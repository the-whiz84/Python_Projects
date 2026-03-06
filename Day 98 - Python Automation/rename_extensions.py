import os
import argparse
from typing import Optional


SYNCTHING_META_DIRS = {".stfolder", ".stversions"}
SYNCTHING_META_PATTERNS = ("~syncthing~", ".syncthing.", ".stignore")


def should_skip_file(filename: str) -> bool:
    """Return True if this file should be ignored for Syncthing safety."""
    if filename.startswith("."):
        return True
    for pattern in SYNCTHING_META_PATTERNS:
        if pattern in filename:
            return True
    return False


def compute_new_extension(
    ext: str,
    from_ext: Optional[str],
    to_ext: Optional[str],
    lowercase: bool,
) -> str:
    """Given a current extension, compute the desired new extension."""
    original_ext = ext

    # Normalize inputs
    if from_ext:
        from_ext = from_ext if from_ext.startswith(".") else f".{from_ext}"
        from_ext = from_ext.lower()
    if to_ext:
        to_ext = to_ext if to_ext.startswith(".") else f".{to_ext}"

    # Optional lowercasing first to avoid case-only churn across devices
    if lowercase:
        ext = ext.lower()

    # Optional explicit mapping (e.g. .mdc -> .md)
    if from_ext and original_ext.lower() == from_ext:
        if to_ext:
            ext = to_ext

    return ext


def safe_rename(old_path: str, new_path: str, dry_run: bool = False) -> None:
    """Rename a file in a Syncthing-safe way, handling case-only changes via a temp name."""
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
    try:
        if os.path.exists(temp_path):
            raise RuntimeError(f"Temp path already exists: {temp_path}")

        os.rename(old_path, temp_path)
        os.rename(temp_path, new_path)
        print(f"Renamed: {os.path.basename(old_path)} -> {os.path.basename(new_path)}")
    except Exception as e:
        print(f"Error renaming {old_path}: {e}")
        if os.path.exists(temp_path) and not os.path.exists(old_path):
            try:
                os.rename(temp_path, old_path)
            except Exception:
                pass


def rename_extensions(
    root_dir: str,
    from_ext: Optional[str] = None,
    to_ext: Optional[str] = None,
    lowercase: bool = True,
    dry_run: bool = False,
) -> None:
    """
    Bulk-rename file extensions so Syncthing can sync them reliably.

    - By default, lowercases all extensions.
    - Optionally remaps a specific extension.
    - Skips Syncthing metadata and temp files.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [
            d
            for d in dirnames
            if not d.startswith(".") and d not in SYNCTHING_META_DIRS
        ]

        for filename in filenames:
            if should_skip_file(filename):
                continue

            name, ext = os.path.splitext(filename)
            if not ext:
                continue

            old_path = os.path.join(dirpath, filename)
            new_ext = compute_new_extension(ext, from_ext, to_ext, lowercase)

            if new_ext == ext:
                continue

            new_filename = name + new_ext
            new_path = os.path.join(dirpath, new_filename)

            if os.path.abspath(old_path) == os.path.abspath(new_path):
                continue

            safe_rename(old_path, new_path, dry_run=dry_run)


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for the bulk extension renamer."""
    parser = argparse.ArgumentParser(
        description="Bulk-rename file extensions in a Syncthing-friendly way."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Root directory to walk (default: current directory).",
    )
    parser.add_argument(
        "--from-ext",
        dest="from_ext",
        default=None,
        help="Only rename files with this extension (e.g. .MDC or MDC).",
    )
    parser.add_argument(
        "--to-ext",
        dest="to_ext",
        default=None,
        help="New extension to apply (e.g. .md). Requires --from-ext.",
    )
    parser.add_argument(
        "--no-lowercase",
        dest="lowercase",
        action="store_false",
        help="Do not automatically lowercase extensions.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would change without renaming anything.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.to_ext and not args.from_ext:
        raise SystemExit("--to-ext requires --from-ext")

    rename_extensions(
        root_dir=args.root,
        from_ext=args.from_ext,
        to_ext=args.to_ext,
        lowercase=args.lowercase,
        dry_run=args.dry_run,
    )
