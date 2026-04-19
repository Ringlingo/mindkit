# MindKit

> **Structured prompts that make your AI think better.**

A **zero-dependency, pure Markdown** framework that gives any LLM focused attention, structured thinking, indexed memory, and reliable safety guardrails.

Not a database. Not a plugin. Just well-organized prompts — and they actually work.

---

## What It Does

Four integrated modules:

| Module | What It Gives You | Example |
|--------|------------------|---------|
| 🎯 **Focus Engine** | Domain-based attention | Mention your keywords → AI loads relevant knowledge |
| ⚡ **Intuition Rules** | Instant patterns from repetition | After 3+ uses, responses become automatic (LTP mechanism) |
| 📋 **Episodic Buffer** | Daily experience index | Recent events weighted higher in retrieval |
| 🛡️ **Safety Guardrails** | Hard rules against destructive ops | Delete/overwrite → always requires confirmation |

---

## Quick Start

### 1. Copy `brain/` to your project

| AI Tool | Where to put `brain/` | How to activate |
|---------|----------------------|-----------------|
| **Claude Code** | `.claude/brain/` | Add `Read .claude/brain/ACTIVATE.md first` to `CLAUDE.md` |
| **Cursor** | `.cursor/brain/` | Reference in `.cursor/rules/mindkit.mdc` |
| **WorkBuddy** | `.workbuddy/brain/` | Use the skill trigger |
| **Any LLM** | Anywhere | Tell it: "Read brain/ACTIVATE.md first" |

### 2. Add your domain

1. Copy `brain/domains/_TEMPLATE.md` → `brain/domains/your_domain.md`
2. Fill in keywords and core knowledge
3. Add domain definition to `brain/FOCUS.md`

### 3. Done

Your AI now has:
- Domain-specific focus (mention your keywords → relevant knowledge activates)
- Thinking tools (say "use First Principles" → structured analysis)
- LTP-enhanced intuition (repeated patterns → faster responses)
- Episodic memory index (recent experiences weighted by recency)
- Safety guardrails (destructive operations always require confirmation)

> 📖 See [TUTORIAL.md](TUTORIAL.md) for detailed usage guide.

---

## The Single-File Version

If you use ChatGPT, Gemini, or any LLM without file access:

1. Open `mindkit-single.md` (included in this repo)
2. Copy its content into your AI's "Custom Instructions" or "System Prompt"
3. Done — the AI understands the framework from text alone

---

## Architecture

```
brain/
├── ACTIVATE.md       ⭐ Entry point — AI reads this first
├── FOCUS.md          🎯 Attention engine + domain definitions
├── EPISODES.md       📋 Episodic buffer — daily experience index
├── INTUITION.md      ⚡ Intuition rules with LTP enhancement
├── THINKKIT.md       🔧 Thinking tools (16 methods)
├── META.md           🛡️ Safety guardrails
└── domains/          📦 Your project domain knowledge
    ├── _TEMPLATE.md
    └── example_*.md
```

**Loading strategy**: ACTIVATE.md is the only required read. Everything else loads on demand.

---

## Compatibility

| LLM | Best Approach | Notes |
|-----|--------------|-------|
| Claude | Natural language protocols | Best at implicit context |
| GPT-4 | Structured YAML/tables | Prefers explicit instructions |
| Gemini | Structured format | Long-context advantage |
| Qwen | Structured + Chinese | Chinese-native |
| DeepSeek | Brief structured | Clear reasoning chains |

---

## Advanced Mode (Optional)

```bash
pip install -r tools/requirements.txt

# Generate a new domain from template
python tools/domain_generator.py --name "my_project" --keywords "code,dev,api"

# Validate your brain/ configuration
python tools/validator.py

# Sync between personal and OSS versions
python tools/sync_manager.py --personal /path/to/project --direction pull
```

See [docs/advanced-mode.md](docs/advanced-mode.md) for details.

---

## Contributing

We welcome contributions! See the [contributing guide](docs/contributing.md).

Areas where we especially need help:
- 🌍 Translations
- 📦 New domain templates
- 🔧 Tool improvements
- 📊 Real-world use cases

---

## License

MIT License — use it however you want.

---

*MindKit: Because "think about it" works better when you have tools for thinking.*
