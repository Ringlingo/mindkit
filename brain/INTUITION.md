# ⚡ MindKit — Intuition Memory

> **Role**: Quick-response rules — patterns compressed into "instant reactions"
> **Neuroscience Basis**: Hippocampal LTP (Long-Term Potentiation) — repeated activation → synaptic strengthening → faster response

---

## Core Mechanism

```
Usage count ↑ → Trigger threshold ↓ → More automatic response
```

| Usage Count | Trigger Threshold | Behavior |
|------------|------------------|----------|
| 1-2 uses | Requires explicit match | Cautious confirmation |
| 3-5 uses | Fuzzy match triggers | Starts becoming automatic |
| 6+ uses | Near-instant | Reflex-like response |

---

## Active Rules

| ID | Trigger | Intuitive Response | Strength | Count |
|----|---------|-------------------|----------|-------|
| INT-001 | "don't execute yet" / "analyze only" | Switch to analysis mode, no execution | 0.9 | 5 |
| INT-002 | C: drive / deletion / high-risk ops | Scan → Report → Risk → Wait for confirmation | 0.95 | 4 |

---

## Rule Sources

- **user**: Explicitly specified by user
- **experience**: Compressed from repeated observations
- **system**: Built-in default rules

---

## Adding New Rules

When a pattern first appears, observe it first. Add after 3rd verification:

```yaml
- id: INT-00X
  trigger: "Trigger condition description"
  action: "Intuitive response"
  strength: 0.7      # New rules start at 0.7
  source: experience
  verified_count: 3  # Must be verified 3+ times
  last_used: YYYY-MM-DD
```

---

## Strength Update Rules

After each successful trigger:

```
Success → count+1 → strength+0.02 (max 1.0)
Failure → strength-0.1 → below 0.5 marks for review
```

---

## How It Works (Workflow)

1. **Pattern appears** (1st time) → Observe and remember
2. **Pattern repeats** (2nd time) → Note the recurrence
3. **Pattern verified 3+ times** → Add to active rules
4. **Rule triggers** → Automatic response, count increases
5. **Rule repeatedly succeeds** → Strength increases toward 1.0

---

_Intuition is compressed experience: the more you repeat, the faster it fires._
