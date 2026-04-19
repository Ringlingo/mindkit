# Example: Cursor Integration

This example shows how to integrate MindKit with [Cursor](https://cursor.sh/).

## Setup

### 1. Copy brain/ to your project

```bash
cp -r brain/ /path/to/your-project/.cursor/brain/
```

### 2. Create a Cursor Rule

Create `.cursor/rules/mindkit.mdc` in your project:

```markdown
---
description: MindKit cognitive framework — read brain/ACTIVATE.md first
globs:
alwaysApply: true
---

You have a cognitive framework installed. Follow these protocols:

1. Read `.cursor/brain/ACTIVATE.md` first at the start of every conversation
2. This activates your focus engine, intuition, and episodic buffer
3. When domain keywords are detected, follow the attention engine in `brain/FOCUS.md`
4. Use thinking tools from `brain/THINKKIT.md` when appropriate
5. Check `brain/EPISODES.md` for recent experiences (recency weighted)
6. Respect the safety guardrails defined in `brain/ACTIVATE.md`
```

### 3. Add domain definitions

Edit `.cursor/brain/FOCUS.md` to add your project domains.

## Important Notes

- **Use `.cursor/rules/*.mdc` format** — the legacy `.cursorrules` file is deprecated in Cursor 2026+
- Set `alwaysApply: true` so the rule activates on every conversation
- The `description` field helps Cursor decide when to apply the rule

## What You Get

- Cursor reads `ACTIVATE.md` at session start → activates cognitive framework
- When you mention domain keywords → attention engine focuses on relevant knowledge
- Recent experiences from EPISODES.md are weighted higher
- Thinking tools available on demand → structured analysis and creative thinking
- Intuition rules strengthen with use (LTP mechanism)
- Safety guardrails always active → destructive operations require confirmation

## Alternative: Project Rule via Cursor Settings

You can also create the rule through Cursor's UI:

1. Open **Cursor Settings → Rules → Project Rules**
2. Click **Add New Rule**
3. Name it `mindkit`
4. Paste the rule content above
5. Set type to **Always**
