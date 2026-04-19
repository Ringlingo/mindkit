#!/usr/bin/env python3
"""
MindKit Sync Manager
Sync between your personal MindKit workspace and the OSS version.

Usage:
    # Pull architecture updates from OSS to personal
    python sync_manager.py --personal /path/to/your/project --direction pull

    # Push architecture improvements from personal to OSS
    python sync_manager.py --personal /path/to/your/project --direction push

    # Preview changes (dry run)
    python sync_manager.py --personal /path/to/your/project --direction pull --dry-run

Safety rules:
- NEVER sync personal data (INTUITION.md) to OSS
- NEVER overwrite personal data with OSS templates
- Always create backups before modifying files
"""

import argparse
import difflib
import shutil
import sys
from datetime import datetime
from pathlib import Path

# Files that are SAFE to sync in BOTH directions (architecture only)
SYNC_SAFE_FILES = {
    "ACTIVATE.md": {
        "skip_sections": [],
        "description": "Entry point -- fully shareable",
    },
    "FOCUS.md": {
        "skip_sections": ["recent"],
        "description": "Attention engine -- sync structure, skip personal domains",
    },
    "THINKKIT.md": {
        "skip_sections": [],
        "description": "Thinking tools -- fully shareable",
    },
    "EPISODES.md": {
        "skip_sections": ["recent"],
        "description": "Episodic buffer -- sync structure, skip personal index entries",
    },
    "META.md": {
        "skip_sections": [],
        "description": "Architecture reference -- fully shareable",
    },
}

# Files that are NEVER synced (personal only)
PERSONAL_ONLY = [
    "INTUITION.md",
]


def find_brain_dir(base_path: Path) -> Path:
    """Auto-detect brain/ directory in various AI tool structures."""
    search_paths = [
        base_path / "brain",
        base_path / ".claude" / "brain",
        base_path / ".cursor" / "brain",
        base_path / ".mindkit" / "brain",
    ]
    for path in search_paths:
        if path.exists():
            return path
    return base_path / "brain"


def create_backup(filepath: Path, backup_dir: Path) -> Path:
    backup_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = backup_dir / f"{filepath.name}.{timestamp}.bak"
    shutil.copy2(filepath, backup_path)
    return backup_path


def show_diff(file_old: str, file_new: str, filename: str) -> None:
    diff = difflib.unified_diff(
        file_old.splitlines(keepends=True),
        file_new.splitlines(keepends=True),
        fromfile=f"current/{filename}",
        tofile=f"new/{filename}",
    )
    diff_text = "".join(diff)
    if diff_text:
        print(f"\n  Changes in {filename}:")
        for line in diff_text.splitlines()[:20]:
            print(f"    {line}")
        remaining = len(diff_text.splitlines()) - 20
        if remaining > 0:
            print(f"    ... and {remaining} more lines")
    else:
        print(f"  No changes in {filename}")


def sync_pull(personal_brain: Path, oss_brain: Path, dry_run: bool = False) -> None:
    """Pull architecture updates from OSS version to personal workspace."""
    print(f"Pull: OSS -> Personal")
    print(f"  OSS:      {oss_brain}")
    print(f"  Personal: {personal_brain}")
    print()

    backup_dir = personal_brain.parent / ".sync_temp" / "backups"

    for filename, spec in SYNC_SAFE_FILES.items():
        oss_file = oss_brain / filename
        personal_file = personal_brain / filename

        if not oss_file.exists():
            print(f"  SKIP {filename}: not found in OSS")
            continue

        if not personal_file.exists():
            if dry_run:
                print(f"  WOULD CREATE {filename} from OSS template")
            else:
                shutil.copy2(oss_file, personal_file)
                print(f"  CREATED {filename} from OSS template")
            continue

        oss_content = oss_file.read_text(encoding="utf-8")
        personal_content = personal_file.read_text(encoding="utf-8")

        if oss_content == personal_content:
            print(f"  SAME {filename}: no changes")
            continue

        show_diff(personal_content, oss_content, filename)

        if dry_run:
            print(f"  WOULD UPDATE {filename} (backup first)")
        else:
            backup = create_backup(personal_file, backup_dir)
            print(f"  BACKUP: {backup}")
            ref_path = personal_brain / f"{filename}.oss_reference"
            ref_path.write_text(oss_content, encoding="utf-8")
            print(f"  REFERENCE: {ref_path}")

    # Protect personal files
    for filename in PERSONAL_ONLY:
        print(f"  PROTECT {filename}: personal data, never overwritten")

    print()
    if dry_run:
        print("Dry run complete. No files were modified.")
    else:
        print("Pull complete. Review .oss_reference files and merge manually.")


def sync_push(personal_brain: Path, oss_brain: Path, dry_run: bool = False) -> None:
    """Push architecture improvements from personal workspace to OSS version."""
    print(f"Push: Personal -> OSS")
    print(f"  Personal: {personal_brain}")
    print(f"  OSS:      {oss_brain}")
    print()

    backup_dir = oss_brain.parent / ".sync_temp" / "backups"

    for filename, spec in SYNC_SAFE_FILES.items():
        personal_file = personal_brain / filename
        oss_file = oss_brain / filename

        if not personal_file.exists():
            print(f"  SKIP {filename}: not found in personal workspace")
            continue

        personal_content = personal_file.read_text(encoding="utf-8")
        oss_content = oss_file.read_text(encoding="utf-8") if oss_file.exists() else ""

        if personal_content == oss_content:
            print(f"  SAME {filename}: no changes")
            continue

        show_diff(oss_content, personal_content, filename)

        if dry_run:
            print(f"  WOULD UPDATE {filename} in OSS (backup first)")
        else:
            if oss_file.exists():
                backup = create_backup(oss_file, backup_dir)
                print(f"  BACKUP: {backup}")
            shutil.copy2(personal_file, oss_file)
            print(f"  UPDATED {filename} in OSS")

    # Block personal-only files
    for filename in PERSONAL_ONLY:
        personal_file = personal_brain / filename
        if personal_file.exists():
            print(f"  BLOCK {filename}: personal data, NEVER pushed to OSS")

    print()
    if dry_run:
        print("Dry run complete. No files were modified.")
    else:
        print("Push complete. Review OSS repo before committing.")


def main():
    parser = argparse.ArgumentParser(
        description="Sync MindKit between personal workspace and OSS version"
    )
    parser.add_argument("--personal", required=True,
                        help="Path to your project directory")
    parser.add_argument("--oss", default=None,
                        help="Path to the OSS repo (default: auto-detect)")
    parser.add_argument("--direction", required=True, choices=["pull", "push"],
                        help="pull=OSS->Personal, push=Personal->OSS")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview changes without modifying files")

    args = parser.parse_args()

    personal_brain = find_brain_dir(Path(args.personal))
    oss_brain = find_brain_dir(Path(args.oss)) if args.oss else Path(__file__).parent.parent / "brain"

    if not personal_brain.exists():
        print(f"Personal brain not found: {personal_brain}")
        sys.exit(1)
    if not oss_brain.exists():
        print(f"OSS brain not found: {oss_brain}")
        sys.exit(1)

    print(f"{'DRY RUN: ' if args.dry_run else ''}MindKit Sync")
    print("=" * 50)

    if args.direction == "pull":
        sync_pull(personal_brain, oss_brain, args.dry_run)
    else:
        sync_push(personal_brain, oss_brain, args.dry_run)


if __name__ == "__main__":
    main()
