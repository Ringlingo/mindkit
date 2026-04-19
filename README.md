# ⚠️ Experimental / 实验性质项目

> **This project is an exploration and prototype. Modern AI models already have built-in safety confirmation and behavior mechanisms — Axiom's value as a standalone tool is limited.**
>
> 本项目是一次思路探索。现代模型本身已有内置的安全确认机制，Axiom 作为独立工具价值有限。

---

# Axiom

> **The cognitive layer that makes AI reliable.**

[![CI](https://github.com/RingLingo/axiom/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/RingLingo/axiom/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Last Commit](https://img.shields.io/github/last-commit/RingLingo/axiom/main.svg)](https://github.com/RingLingo/axiom/commits/main)

**Axiom** is a zero-dependency cognitive layer for AI agents and assistants. It makes AI interactions predictable, safe, and consistent — using only Markdown files you control.

Think of it as **installing good judgment into your AI**: it knows what not to destroy, what to remember, how to think through problems, and when to ask instead of assume.

---

## The 5 Laws

These are not guidelines. They are the laws of every Axiom-powered AI.

| Law | What It Means |
|-----|--------------|
| **I: Preservation** | Never destroy without explicit confirmation |
| **II: Boundaries** | Never touch system files or unauthorized data |
| **III: Truth** | Never lie, hide uncertainty, or fabricate |
| **IV: Context** | Never forget project knowledge or user preferences |
| **V: Authorization** | External action requires explicit approval |

These five laws make the difference between an AI that is *capable* and an AI that is *trustworthy*.

---

## What Axiom Gives You

| Module | What It Does |
|--------|-------------|
| **AXIOM** | 5 unbreakable laws — always active, cannot be bypassed |
| **FOCUS** | Keyword-triggered knowledge loading — know what project you're in |
| **CONTEXT** | AI-writable living log — project state persists across sessions |
| **RULES** | Standing instructions — you say it once, AI follows it always |
| **THINK** | 20 structured thinking methods — when analysis is needed |

---

## Quick Start

### 1. Copy `brain/` into your project

| AI Tool | Where | How |
|---------|-------|-----|
| **Claude Code** | `.claude/brain/` | Add to `CLAUDE.md` |
| **Cursor** | `.cursor/brain/` | Add to `.cursor/rules/` |
| **WorkBuddy** | `.workbuddy/brain/` | Skill trigger |
| **Any LLM** | Anywhere | Tell it: "Read brain/ACTIVATE.md first" |

### 2. Fill in your project knowledge

Copy `brain/domains/_TEMPLATE.md` → your domain file, then add to `FOCUS.md`.

### 3. Start talking

> "This is my React project, using Next.js and Prisma."

AI automatically loads your domain knowledge. AXIOM laws are always active.

---

## Single-File Version

No file access? ChatGPT, Gemini, or any LLM:

1. Open `axiom-single.md`
2. Copy into your AI's "Custom Instructions"
3. Done

---

## Architecture

```
brain/
├── ACTIVATE.md       ⭐ Entry point — read first, every session
├── AXIOM.md         ⚖️ 5 laws — always active, cannot be bypassed
├── FOCUS.md         🎯 Keyword → domain knowledge mapping
├── CONTEXT.md       📝 AI-writable project log (state persists)
├── RULES.md         📋 Standing instructions (you write, AI follows)
├── THINK.md         🧠 20 thinking methods (on demand)
└── domains/         📦 Your project knowledge
    ├── _TEMPLATE.md
    └── example_*.md
```

**Axiom is loaded once. It works forever.**

---

## Why Axiom Exists

Most AI problems are not about intelligence. They are about judgment:

> *"I told it to clean up the logs and it deleted production data."*
> *"It keeps forgetting my project conventions."*
> *"It tried to send an email without asking."*

**AXIOM solves the judgment problem.** The five laws prevent destruction. FOCUS and CONTEXT provide continuity. RULES captures preferences. THINK structures reasoning.

---

## Compatibility

| LLM / Tool | Works? | Best For |
|-----------|--------|---------|
| Claude Code | ✅ | Best — native file access |
| Cursor | ✅ | Rule-based activation |
| WorkBuddy | ✅ | Skill trigger |
| GPT-4 / o1 / o3 | ✅ | Via axiom-single.md |
| Gemini | ✅ | Via axiom-single.md |
| Qwen | ✅ | Structured prompts |
| DeepSeek | ✅ | Brief structured formats |

---

## Advanced Tools

```bash
pip install -r tools/requirements.txt

python tools/validator.py              # Validate your brain/ setup
python tools/domain_generator.py \
  --name "my_project" \
  --keywords "react,api,typescript"
python tools/sync_manager.py \
  --personal /path \
  --direction pull
```

---

## Contributing

See `docs/contributing.md`.

We especially welcome:
- 🌍 Translations
- 📦 New domain templates
- 🔧 Tool improvements
- 📊 Real-world use cases

---

## License

MIT — use it however you want.

---

*Axiom: The laws that make AI trustworthy.*
