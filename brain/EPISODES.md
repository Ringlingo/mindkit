# 📋 MindKit — Episodic Buffer

> **Role**: Index of daily interaction episodes — what happened, when, where, emotional tag
> **Neuroscience Basis**: Episodic Buffer (Baddeley) — integrates experiences with temporal and spatial context

---

## Mechanism

```
Daily interaction → Key event record → EPISODES index → Priority retrieval by recency
```

- Each entry: date + theme + key decisions/outcomes + emotional tag
- Retrieval priority: recency bias (recent events weighted higher)
- Long-unretrieved → archived to deep storage

---

## Index Format

```yaml
episodes:

  - date: YYYY-MM-DD
    theme: "What happened"
    key_events:
      - "Event 1"
      - "Event 2"
    emotion: neutral/positive/negative/breakthrough
    domains: [relevant_domain_tags]

  - date: YYYY-MM-DD
    theme: "Another session"
    key_events:
      - "Decided to use approach X instead of Y"
      - "Discovered that Z doesn't work"
    emotion: breakthrough
    domains: [my_project, debugging]
```

---

## Usage Rules

1. **After each session**: Add new episode if significant work happened
2. **After 30 days**: Move to `archived:` section
3. **Retrieval**: Both by date (reverse chronological) AND by domain keyword

---

## Why This Exists

Unlike explicit knowledge (facts, rules), episodic memory captures *experiences*:
- What approach worked yesterday
- Which path was a dead end last week
- The emotional context of a decision

This mirrors how the brain's hippocampus buffers experiences before they consolidate into long-term semantic memory.

---

_Episodic memory is the index of your journey. Every decision becomes traceable._
