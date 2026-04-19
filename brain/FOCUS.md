# 🎯 MindKit — Attention Engine

> **Role**: Focus on relevant knowledge domains, suppress distractions
> **Created**: 2026-04-17

---

## Core Mechanism

```
User input → Keyword scan → Match a domain?
    │                         │
    ├─ Hit → Load domain's core knowledge
    │
    └─ Miss → Use general thinking tools
```

---

## Project Domain Definitions

> Add your domains here. Copy `domains/_TEMPLATE.md` → fill in → paste definition below.

### Example Domain Templates:

```yaml
# Software Development
domain: software_dev
name: "Software Development"
icon: "💻"
keywords: [code, develop, debug, deploy, API, framework, git, test, refactor]
```

```yaml
# Creative Writing
domain: creative_writing
name: "Creative Writing"
icon: "✍️"
keywords: [story, plot, character, narrative, dialogue, worldbuilding]
```

```yaml
# Data Science
domain: data_science
name: "Data Science"
icon: "📊"
keywords: [data, analysis, model, ML, pipeline, visualization, statistics]
```

---

## Adding New Domains

1. Copy `domains/_TEMPLATE.md` → `domains/your_domain.md`
2. Fill in keywords and core knowledge
3. Add domain definition above

---

## File Index

```yaml
domains/:
  your_domain.md     → Your project domain knowledge
  _TEMPLATE.md      → Template for new domains
```

---

_Attention engine: Make every thinking session focus on what matters._
