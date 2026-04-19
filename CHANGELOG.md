# MindKit Changelog

All notable changes to MindKit will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2026-04-19

### Added
- **EPISODES.md**: Episodic buffer — daily experience index with recency bias (neuroscience: Baddeley's Episodic Buffer)
- **LTP Enhancement**: Intuition rules now strengthen with use (neuroscience: Hippocampal Long-Term Potentiation)
- **FRAGMENT:recent**: Recent usage tracking in domain files
- **Detailed TUTORIAL.md**: Comprehensive usage guide with step-by-step instructions
- **CITATIONS.md**: Academic references and neuroscience foundations
- **PURPOSE.md**: Development purpose and design philosophy

### Changed
- **ACTIVATE.md**: Updated startup sequence to include EPISODES and LTP mechanism
- **FOCUS.md**: Simplified — removed macro layer (knowledge classification tree)
- **INTUITION.md**: Replaced decay mechanism with LTP enhancement
- **THINKKIT.md**: Removed FRAGMENT tags, simplified to catalog only
- **META.md**: Removed growth stages (Stage 0-5), removed token budget, kept safety only
- **README.md / README_CN.md**: Updated to v2.1 architecture

### Removed
- **PALACE.md**: Memory palace (superseded by simpler EPISODES.md)
- **experience/**: Empty template files (3 files + directory)
- **Macro layer**: Knowledge classification tree and affinity matrix
- **Growth stages**: Stage 0-5 conceptual framework
- **Token budget allocation**: Simplified loading strategy
- **usage_stats / tool_usage**: Unused tracking fields

### Philosophy Change
Old: "Give your AI a brain" (implies consciousness)
New: "Structured prompts that make your AI think better" (honest, verifiable)

---

## [1.0.0] - 2026-04-17

### Added
- Core cognitive framework: Focus Engine, ThinkKit, Intuition Rules, Memory Palace, Safety Guardrails
- Dual-layer knowledge architecture (macro categories + micro domains)
- 16 thinking tools in 4 categories (Analytical, Creative, Verification, Guidance)
- Memory Palace (PALACE.md): 5-room indexed storage with keyword/ID retrieval and split memory links
- Domain template with creation guide
- 3 example domains (software dev, creative writing, data science)
- Single-file version (`mindkit-single.md`) for LLMs without file access
- Python tools: domain_generator, validator, sync_manager
- IDE integration examples: Claude Code, Cursor, generic LLM, skill integration
- Documentation: user guide, advanced mode, contributing guide
- GitHub config: issue templates, PR template, .gitignore
- MIT License

### Design Principles
- Zero dependency — pure Markdown core
- Fragmented loading — only read what you need
- Privacy-first — personal data never leaves your workspace
- Honest positioning — structured prompts, not artificial consciousness
