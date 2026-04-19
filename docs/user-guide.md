# MindKit User Guide

How to use MindKit with different AI tools and workflows.

---

## For Developers (Claude Code / Cursor)

### Setup

```bash
# 1. Clone the repo
git clone https://github.com/MindKit-Project/mindkit.git

# 2. Copy brain/ into your project
cp -r mindkit/brain/ your-project/.claude/brain/

# 3. Add activation instruction
echo "Read .claude/brain/ACTIVATE.md first at every session start." >> your-project/CLAUDE.md
```

> **Replace the URL with your actual repository address after creating the repo on GitHub.**

### Adding Your First Domain

1. Copy the template:
   ```bash
   cp brain/domains/_TEMPLATE.md brain/domains/my_project.md
   ```

2. Edit `my_project.md` — fill in:
   - Core Knowledge: paths to your project files
   - Keywords: terms that should trigger this domain

3. Add the domain definition to `brain/FOCUS.md`

4. Done! Next time you mention those keywords, the attention engine activates.

### Verifying It Works

After adding a domain, test it:
1. **Run the validator**: `python tools/validator.py`
2. **Test in conversation**: Mention one of your domain's keywords
3. **Check the response**: AI should reference domain-specific knowledge

If the AI doesn't activate the domain:
- Check that the domain definition is in FOCUS.md
- Check that keywords match what you're typing
- Check that the domain file has `==FRAGMENT:core==` and `==END==` tags

---

## For Non-Developers (ChatGPT / Gemini / etc.)

### Quick Setup

1. Open `mindkit-single.md` from this repo
2. Copy its content into your AI's Custom Instructions
3. Edit the domains section to match your work
4. Done — the AI now has the framework

### Without File Access

If your AI can't read files, just paste the content:
1. First message: "Here is your thinking framework. Follow it."
2. Paste the content of `mindkit-single.md`
3. The AI will follow the protocols from text alone

---

## For Teams

### Shared Brain

1. One person maintains `brain/` in the project repo
2. Everyone points their AI tool to the same `brain/` location
3. Shared domains and thinking tools, individual intuition rules
4. Add `INTUITION.md` to `.gitignore` for personal rules

---

## Common Workflows

| I want to... | What to do |
|-------------|-----------|
| Make AI understand my project | Add a domain in `brain/domains/`, define keywords |
| Make AI think more systematically | Ask it to use a specific thinking tool: "Use First Principles" |
| Make AI remember my preferences | Add intuition rules to `brain/INTUITION.md` (LTP-enhanced) |
| Track recent experiences | Add entries to `brain/EPISODES.md` |
| Use with ChatGPT (no file access) | Copy `mindkit-single.md` into Custom Instructions |
| Sync improvements back to OSS | Use `python tools/sync_manager.py --personal /path --direction push --dry-run` |

---

## Compatibility & Practical Analysis

### Environment Compatibility

| Category | Tool | File Access | Setup Method | Functionality |
|----------|------|------------|-------------|---------------|
| **AI Coding Tools** | Claude Code | ✅ Full | `.claude/brain/` | Full |
| | Cursor | ✅ Full | `.cursor/brain/` | Full |
| | Cline | ✅ Full | `.cline/brain/` | Full |
| | Continue.dev | ✅ Full | `.continue/brain/` | Full |
| **Chat-based LLMs** | ChatGPT | ❌ None | `mindkit-single.md` → Custom Instructions | Thinking Tools + Safety + Intuition |
| | Gemini | ❌ None | `mindkit-single.md` → System Instructions | Thinking Tools + Safety + Intuition |
| | DeepSeek | ❌ None | `mindkit-single.md` → System Prompt | Thinking Tools + Safety + Intuition |
| | Qwen | ❌ None | `mindkit-single.md` → System Prompt | Thinking Tools + Safety + Intuition |
| | Claude Web | ❌ None | `mindkit-single.md` → Custom Instructions | Thinking Tools + Safety + Intuition |
| **API-based** | OpenAI API | ⚠️ If you build it | System message in API call | Thinking Tools + Safety |
| | Anthropic API | ⚠️ If you build it | System prompt in API call | Thinking Tools + Safety |
| | Google AI API | ⚠️ If you build it | System instruction in API call | Thinking Tools + Safety |
| **Local LLMs** | LM Studio | ⚠️ Depends | System prompt | Thinking Tools + Safety |
| | Ollama | ⚠️ Depends | System prompt | Thinking Tools + Safety |

**Legend**: ✅ Full = All 5 modules | ⚠️ Partial = Depends on implementation | ❌ Limited = mindkit-single.md only

---

### Functionality Analysis

#### 🎯 Focus Engine
| Environment | Works? | How |
|-------------|--------|-----|
| File-based AI tools | ✅ Full | Reads `FOCUS.md` + `domains/*.md` |
| Chat LLMs (single.md) | ✅ Full | Keywords defined in prompt |
| API-based | ✅ Full | Pass domains in system prompt |

**Practical Value**: ⭐⭐⭐⭐⭐
- Works everywhere with same mechanism
- Clear, immediate benefit: AI focuses on relevant knowledge

---

#### ⚡ Intuition Rules (LTP)
| Environment | Works? | How |
|-------------|--------|-----|
| File-based AI tools | ✅ Full | Reads `INTUITION.md`, persists across sessions |
| Chat LLMs (single.md) | ⚠️ Limited | Rules in prompt, resets each conversation |
| API-based | ⚠️ Limited | Pass rules in system prompt, no persistence |

**Practical Value**: ⭐⭐⭐
- Best with persistent storage (file-based tools)
- For chat LLMs: accumulates within session, not across sessions
- LTP strengthening requires repeated use → benefits long-term relationships

---

#### 📋 Episodic Buffer
| Environment | Works? | How |
|-------------|--------|-----|
| File-based AI tools | ✅ Full | Reads `EPISODES.md`, appends new entries |
| Chat LLMs (single.md) | ❌ None | No persistent storage |
| API-based | ❌ None | No external storage by default |

**Practical Value**: ⭐⭐
- Only works with file-based tools
- Requires manual maintenance (add entries after sessions)
- Most useful for recurring projects

---

#### 🔧 Thinking Tools
| Environment | Works? | How |
|-------------|--------|-----|
| All environments | ✅ Full | Defined in prompts, no persistence needed |
| File-based AI tools | ✅ Full | `THINKKIT.md` + full detail |
| Chat LLMs (single.md) | ✅ Full | Catalog in single file |
| API-based | ✅ Full | Include tool definitions in system prompt |

**Practical Value**: ⭐⭐⭐⭐⭐
- Works everywhere
- Immediate benefit: structured thinking on complex problems
- No persistence needed → works perfectly in stateless environments

---

#### 🛡️ Safety Guardrails
| Environment | Works? | How |
|-------------|--------|-----|
| All environments | ✅ Full | Hard-coded in system prompt |
| File-based AI tools | ✅ Full | `META.md` |
| Chat LLMs (single.md) | ✅ Full | In single file |
| API-based | ✅ Full | In system prompt |

**Practical Value**: ⭐⭐⭐⭐⭐
- Works everywhere with same effect
- Critical protection: prevents destructive operations
- Especially valuable for automated/API scenarios

---

### Quick Decision Guide

**Choose your setup based on your tool:**

```
┌─────────────────────────────────────────────────────────────┐
│  What AI tool do you use?                                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Claude Code / Cursor / Cline / Continue                      │
│  → Use file-based setup (brain/) → FULL FUNCTIONALITY        │
│                                                              │
│  ChatGPT / Gemini / DeepSeek / Qwen / Claude Web             │
│  → mindkit-single.md → Custom Instructions               │
│  → Gets: Thinking Tools + Safety + Intuition (session-only)  │
│                                                              │
│  API-based (OpenAI / Anthropic / etc.)                      │
│  → Include mindkit-single.md content in system prompt   │
│  → Gets: Thinking Tools + Safety                            │
│                                                              │
│  Local LLM (LM Studio / Ollama)                            │
│  → Set MindKit content as system prompt                 │
│  → Gets: Thinking Tools + Safety                            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

### What You'll Actually Get

| Setup | Focus | Thinking Tools | Safety | Intuition | Episodes |
|-------|--------|---------------|--------|-----------|---------|
| **File-based (Claude Code etc.)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **mindkit-single.md (ChatGPT etc.)** | ✅ | ✅ | ✅ | ⚠️ Session only | ❌ |
| **API / Local LLM** | ✅ | ✅ | ✅ | ⚠️ No persistence | ❌ |

**Bottom line**: Even the simplest setup (single file in ChatGPT) gives you focused attention + thinking tools + safety. The file-based setup adds cross-session memory via intuition and episodic buffer.

---

### Recommended Combinations

**For daily coding work (Claude Code / Cursor)**:
- Full setup with all modules
- Add project-specific domains
- Accumulate intuition rules over time
- Track episodic entries for complex projects

**For research / analysis (ChatGPT / Gemini)**:
- mindkit-single.md in Custom Instructions
- Focus on thinking tools for structured analysis
- Safety guardrails active
- Manually track important decisions

**For API integrations ( developers)**:
- Include core prompts in system message
- Build custom storage for intuition/episodes if needed
- Safety guardrails prevent costly mistakes

---

## FAQ

**Q: Do I need to read all brain files every conversation?**
A: No. ACTIVATE.md is the only required read (~500 tokens). Other files load on demand.

**Q: Can I use MindKit without file system access?**
A: Yes. Use `mindkit-single.md` — paste it into Custom Instructions. You get Thinking Tools + Safety + Intuition (within session).

**Q: How does intuition strengthen?**
A: LTP (Long-Term Potentiation) mechanism: repeated use → lower trigger threshold → faster response. 3-5 uses: fuzzy trigger; 6+ uses: near-instant.

**Q: Can multiple team members share the same brain/?**
A: Yes. Share everything except `INTUITION.md` (that's personal).

**Q: I'm on Windows. Do the bash commands work?**
A: Replace `cp -r` with `xcopy /E /I` or PowerShell `Copy-Item -Recurse`. The Python tools work on all platforms.

**Q: What's the minimum setup to get value?**
A: Paste `mindkit-single.md` into ChatGPT's Custom Instructions. Takes 2 minutes, gives you structured thinking + safety immediately.

**Q: Does episodic buffer work in chat LLMs?**
A: No, but you can simulate it by keeping a running summary in your conversation and referencing it: "Here's what we worked on last time: ..."

---

_MindKit grows with you. The more domains and rules you add, the more focused it gets._
