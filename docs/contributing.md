# Contributing to MindKit

Thank you for your interest!

## Ways to Contribute

### 🐛 Bug Reports
- Found a structural issue? Open an issue with: which file, what's wrong, what you expected.

### 📦 New Domain Templates
- Create a domain following `_TEMPLATE.md`
- Use `python tools/domain_generator.py --name "..." --category "..."`
- Make sure it's generic (no personal data)

### 🌍 Translations
- Translate README or docs into your language
- Keep technical terms in English where appropriate

### 🔧 Tool Improvements
- Improve Python scripts in `tools/`
- Keep dependencies minimal

### 📊 Real-World Use Cases
- Share how MindKit helped you
- BEFORE/AFTER examples are especially valuable

## Development Workflow

1. Fork the repo
2. Create a feature branch: `git checkout -b my-feature`
3. Make your changes
4. Validate: `python tools/validator.py`
5. Commit with a clear message
6. Push and create a Pull Request

## File Naming Conventions

- Brain files: `UPPERCASE.md` (ACTIVATE.md, FOCUS.md, etc.)
- Domain files: `snake_case.md` (example_software_dev.md)
- Tool files: `snake_case.py` (domain_generator.py)
- Doc files: `kebab-case.md` (advanced-mode.md)

## Privacy Rules

**NEVER include personal data in contributions:**
- No real names, emails, or phone numbers
- No API keys or passwords
- No specific project details that could identify someone
- Use generic examples

## Code of Conduct

- Be respectful
- Focus on constructive feedback
- No personal data in contributions
- Keep discussions in English for accessibility
