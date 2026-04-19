# MindKit Advanced Mode — Python Tools

MindKit works in pure Markdown by default. The Python tools add enhanced capabilities.

## Installation

```bash
pip install -r tools/requirements.txt
```

Dependencies: `pyyaml`, `rich`, `click`

## Tools

### 1. Domain Generator

```bash
# Basic usage
python tools/domain_generator.py --name "My Project"

# With custom keywords
python tools/domain_generator.py --name "Marketing" --keywords "campaign,brand,analytics"

# With custom icon
python tools/domain_generator.py --name "Data Science" --keywords "data,ml,analytics" --icon "📊"

# Custom output path
python tools/domain_generator.py --name "My Project" --output /path/to/domains/my_project.md
```

### 2. Brain Validator

```bash
# Validate default brain/ location
python tools/validator.py

# Validate a specific path
python tools/validator.py --path /path/to/brain
```

Checks:
- All required files exist
- Required sections are present
- YAML blocks are properly closed
- Domain files have FRAGMENT tags

### 3. Sync Manager

Sync between personal workspace and OSS version:

```bash
# Pull updates from OSS to personal
python tools/sync_manager.py --personal /path/to/your/project --direction pull

# Push improvements from personal to OSS
python tools/sync_manager.py --personal /path/to/your/project --direction push

# Preview changes (dry run)
python tools/sync_manager.py --personal /path/to/your/project --direction pull --dry-run
```

**Safety**: `INTUITION.md` is NEVER synced (personal data). Backups created before modifications.

## Shell Aliases

```bash
# Add to ~/.bashrc or ~/.zshrc
alias nc-validate="python /path/to/mindkit/tools/validator.py"
alias nc-domain="python /path/to/mindkit/tools/domain_generator.py"
alias nc-sync="python /path/to/mindkit/tools/sync_manager.py"
```
