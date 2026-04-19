# MindKit Quick Start — 3 Steps to a Focused AI

## Step 1: Copy the Brain

Copy `brain/` into your project. Where it goes depends on your AI tool:

### Claude Code

```bash
cp -r brain/ /path/to/your-project/.claude/brain/
```

Add to `CLAUDE.md`:
```
Read .claude/brain/ACTIVATE.md first at the start of every conversation.
```

### Cursor

```bash
cp -r brain/ /path/to/your-project/.cursor/brain/
```

Create `.cursor/rules/mindkit.mdc`:
```markdown
---
description: MindKit cognitive framework
globs:
alwaysApply: true
---

Read .cursor/brain/ACTIVATE.md first at the start of every conversation.
```

### Any LLM (ChatGPT, Gemini, etc.)

Copy the content of `mindkit-single.md` into your AI's Custom Instructions.

## Step 2: Add Your First Domain

1. Copy `brain/domains/_TEMPLATE.md` → `brain/domains/my_domain.md`
2. Fill in keywords and core knowledge
3. Add the domain definition to `brain/FOCUS.md`

Example:
```yaml
domain: web_dev
name: "Web Development"
icon: "💻"
keywords: [react, vue, css, api, frontend, backend]
```

## Step 3: Use It

- **Domain focus**: Mention your keywords → AI concentrates on relevant knowledge
- **Thinking tools**: "Use First Principles to analyze this" → structured output
- **Intuition rules**: After repeating patterns, add quick-response rules to INTUITION.md
- **Safety**: Destructive operations always require your confirmation

### Quick Test

Start a conversation and say: "Tell me what you know about [one of your domain keywords]"

If the AI references domain-specific knowledge from your domain file, it's working.

## Optional: Advanced Mode

```bash
pip install -r tools/requirements.txt

# Generate a domain from template
python tools/domain_generator.py --name "My Project" --keywords "code,dev,api"

# Validate your brain/ setup
python tools/validator.py
```

---

_That's it. Three steps. Five minutes._
