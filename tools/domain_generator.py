#!/usr/bin/env python3
"""
MindKit Domain Generator
Generate a new domain knowledge cluster from template.

Usage:
    python domain_generator.py --name "my_project"
    python domain_generator.py --name "my_project" --keywords "code,dev,api"
    python domain_generator.py --name "Marketing" --icon "📢"
"""

import argparse
import re
from datetime import date
from pathlib import Path


TEMPLATE = '''# {icon} Domain Knowledge Cluster — {name_display}

> **Mounted under**: FOCUS.md → {domain_id} domain
> **Created**: {today}

---

==FRAGMENT:core==

## Core Knowledge

- **Related files**: [path to domain-specific files]
- **Key resources**: [documentation, references, etc.]

## Key Concepts

- [Concept 1]
- [Concept 2]
- [Concept 3]

==END==

---

==FRAGMENT:recent==

## Recent Usage

| Date | Event | Status |
|------|-------|--------|
| YYYY-MM-DD | [What happened] | [completed/in-progress] |

==END==

---

==FRAGMENT:deep==

## Deep Knowledge (Load on demand)

### [Sub-topic 1]
- Detail 1
- Detail 2

### [Sub-topic 2]
- Detail 1
- Detail 2

==END==

---

## How to Add This Domain

1. Copy this file → rename to `domains/{domain_id}.md`
2. Fill in your core knowledge and preferences
3. Add to FOCUS.md:

```yaml
domain: {domain_id}
name: "{name_display}"
icon: "{icon}"
keywords: [{keywords_yaml}]
```

---

_This is a template. Copy it, fill it in, and add to FOCUS.md._
'''


ICONS = {
    "technology": "💻",
    "creative": "✍️",
    "research": "🔬",
    "business": "📊",
    "design": "🎨",
    "data": "📈",
    "default": "🏷️",
}


def to_domain_id(name: str) -> str:
    """Convert display name to snake_case domain ID."""
    result = re.sub(r'[^\w\s]', '', name.lower())
    result = re.sub(r'\s+', '_', result)
    return result


def guess_icon(name: str) -> str:
    """Guess icon from name keywords."""
    name_lower = name.lower()
    for key, icon in ICONS.items():
        if key in name_lower:
            return icon
    return ICONS["default"]


def generate_domain(name: str, keywords: list = None, icon: str = None) -> str:
    """Generate domain markdown content."""
    domain_id = to_domain_id(name)
    icon = icon or guess_icon(name)
    today = date.today().isoformat()

    keywords = keywords or [domain_id]
    keywords_yaml = ", ".join(keywords)

    return TEMPLATE.format(
        icon=icon,
        name_display=name,
        domain_id=domain_id,
        today=today,
        keywords_yaml=keywords_yaml,
    )


def main():
    parser = argparse.ArgumentParser(description="Generate a MindKit domain file")
    parser.add_argument("--name", required=True, help="Domain display name (e.g. 'My Project')")
    parser.add_argument("--keywords", default="", help="Comma-separated keywords")
    parser.add_argument("--icon", default=None, help="Emoji icon (e.g. '💻')")
    parser.add_argument("--output", default=None, help="Output file path (default: brain/domains/<domain_id>.md)")

    args = parser.parse_args()

    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()] if args.keywords else None
    content = generate_domain(args.name, keywords, args.icon)

    domain_id = to_domain_id(args.name)

    if args.output:
        output_path = Path(args.output)
    else:
        # Default: save to brain/domains/
        script_dir = Path(__file__).parent.parent
        output_path = script_dir / "brain" / "domains" / f"{domain_id}.md"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")

    print(f"✅ Domain generated: {output_path}")
    print(f"   Domain ID: {domain_id}")
    print(f"   Next: Add the domain definition to FOCUS.md")


if __name__ == "__main__":
    main()
