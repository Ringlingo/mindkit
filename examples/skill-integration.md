# MindKit as a WorkBuddy / Claude Code Skill

> If you use an AI tool that supports "Skills" or "Custom Instructions", you can load MindKit as a skill.

---

## Method 1: WorkBuddy Skill (Recommended for WorkBuddy users)

1. Copy the `记忆中枢/` skill folder to your `.workbuddy/skills/` directory
2. Edit `SKILL.md` to point to your brain/ location
3. WorkBuddy will auto-load the skill at conversation start
4. The skill triggers the MindKit startup sequence

## Method 2: Claude Code CLAUDE.md Integration

Add this to your project's `CLAUDE.md`:

```markdown
# MindKit Cognitive Framework

Read .claude/brain/ACTIVATE.md first at every session start.
Follow its startup sequence to activate the framework.

Key protocols:
- Focus: Scan FOCUS.md for domain matches based on user keywords
- Episodes: Check EPISODES.md for recent experiences (recency weighted)
- Intuition: Check INTUITION.md for quick-response rules (LTP enhanced)
- Thinking: Load THINKKIT.md tools on demand (catalog first)
- Safety: Never auto-execute destructive operations (HR-001 to HR-005)
```

## Method 3: Cursor Rules

Create `.cursor/rules/mindkit.mdc`:

```markdown
---
description: MindKit cognitive framework — read brain/ACTIVATE.md first
globs:
alwaysApply: true
---

Read .cursor/brain/ACTIVATE.md first at the start of every conversation.
This is your cognitive framework — follow its protocols.
```

## Method 4: Any LLM (Manual Paste)

1. Open `brain/ACTIVATE.md` and copy its full content
2. Paste into your AI's "Custom Instructions" or "System Prompt"
3. Optionally also paste `brain/FOCUS.md` content
4. The AI will follow the protocols from the text alone

---

## How It Works

```
Skill/CLAUDE.md/.mdc triggers
    ↓
AI reads ACTIVATE.md (~500 tokens)
    ↓
Startup sequence activates:
  1. Scan FOCUS.md → match user's topic to a domain
  2. Check EPISODES.md → recent experiences (recency weighted)
  3. If domain hit → load domain knowledge
  4. Check INTUITION.md → quick-response rules (LTP enhanced)
  5. Load THINKKIT.md tools → when analysis needed
    ↓
Full cognitive framework is active
```

---

_The skill is just a trigger. The architecture is in the files._
