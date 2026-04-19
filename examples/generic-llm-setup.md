# Example: Generic LLM Integration

This example shows how to use MindKit with any LLM (ChatGPT, Gemini, DeepSeek, Qwen, etc.) that supports custom instructions or system prompts.

## Setup

### 1. Copy brain/ into your project

```bash
cp -r brain/ /path/to/your-project/brain/
```

### 2. Add to your system prompt / custom instructions

Copy this into your LLM's system prompt or custom instructions field:

```
You have a cognitive framework installed. Follow these protocols:

1. Read brain/ACTIVATE.md first at the start of every conversation
2. This activates your focus engine, episodic buffer, and intuition systems
3. When domain keywords are detected, follow the attention engine in brain/FOCUS.md
4. Use thinking tools from brain/THINKKIT.md when appropriate
5. Check EPISODES.md for recent experiences (recency weighted)
6. Respect the safety guardrails defined in brain/ACTIVATE.md
```

### 3. For Chat-based LLMs (no file access)

If your LLM cannot read local files, paste the content directly:

1. Open `mindkit-single.md` and paste its content into your "Custom Instructions" or "System Prompt"
2. The LLM will understand the framework from the text alone

**Tip**: For long-term use with chat-based LLMs, consider:
- Pasting `mindkit-single.md` content into your "Custom Instructions" field
- Keeping the content updated as you add new domains and intuition rules

## LLM-Specific Tips

| LLM | Best Approach | Notes |
|-----|--------------|-------|
| **ChatGPT** | Custom Instructions + Memory | Paste mindkit-single.md into Custom Instructions |
| **Gemini** | System Instructions | Use structured format |
| **DeepSeek** | System prompt | Keep instructions brief — prefers concise prompts |
| **Qwen** | System prompt (Chinese) | Supports both channels, Chinese-native |
| **Any API** | System message | Include mindkit-single.md content |

## What You Get

- Structured cognitive protocols instead of ad-hoc prompting
- Attention engine that focuses on relevant knowledge domains
- 16 thinking tools for systematic analysis
- Episodic buffer for recent experiences (recency weighted)
- Safety guardrails built into the architecture
- Intuition rules that strengthen with use (LTP mechanism)
