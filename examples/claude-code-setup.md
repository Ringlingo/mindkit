# Example: Claude Code Integration

This example shows how to integrate MindKit with [Claude Code](https://code.claude.com/).

## Setup

### 1. Copy brain/ to your project

```bash
cp -r brain/ /path/to/your-project/.claude/brain/
```

### 2. Configure CLAUDE.md

Create or edit `CLAUDE.md` in your project root:

```markdown
# Project Configuration

## Cognitive Architecture

Read .claude/brain/ACTIVATE.md first at the start of every conversation.
This is your cognitive architecture — follow its protocols.

Key files:
- `.claude/brain/ACTIVATE.md` — Activation card, entry point (READ FIRST)
- `.claude/brain/FOCUS.md` — Attention engine and domain definitions
- `.claude/brain/EPISODES.md` — Episodic buffer, recent experience index
- `.claude/brain/THINKKIT.md` — 16 thinking tools (load on demand)
- `.claude/brain/INTUITION.md` — Intuition rules with LTP enhancement
- `.claude/brain/META.md` — Safety guardrails (details)
```

### 3. Add domain definitions

Edit `.claude/brain/FOCUS.md` to add your project domains.

## What You Get

- Claude reads `ACTIVATE.md` at session start → activates cognitive framework
- When you mention domain keywords → attention engine focuses on relevant knowledge
- Recent experiences from EPISODES.md are weighted higher (recency bias)
- Thinking tools available on demand → structured analysis and creative thinking
- Intuition rules strengthen with use (LTP mechanism)
- Safety guardrails always active → destructive operations require confirmation

## Pro Tip: Minimal CLAUDE.md

For the simplest setup, just add one line to `CLAUDE.md`:

```
Read .claude/brain/ACTIVATE.md first. Follow its cognitive framework protocols.
```

Everything else is defined inside the brain/ files themselves.
