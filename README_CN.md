# MindKit

> **结构化提示词，让你的 AI 思考得更好。**

一个**零依赖、纯 Markdown** 的框架，让任何 LLM 获得聚焦注意力、LTP强化直觉、情景索引记忆和可靠的安全护栏。

不是数据库。不是插件。只是一组组织良好的提示词——而且它们真的有效。

---

## 它做什么

四个协同工作的模块：

| 模块 | 给你什么 | 示例 |
|------|---------|------|
| 🎯 **注意力引擎** | 基于域的注意力 | 提到你的关键词 → AI 加载相关知识 |
| ⚡ **直觉规则** | 来自重复的即时模式 | 3次以上使用后，反应变得更自动（LTP机制） |
| 📋 **情景缓冲区** | 每日经历索引 | 近期事件在检索时权重更高 |
| 🛡️ **安全护栏** | 针对破坏性操作的硬规则 | 删除/覆盖 → 始终需要确认 |

---

## 快速开始

### 1. 将 `brain/` 复制到你的项目

| AI 工具 | 存放位置 | 激活方式 |
|---------|---------|---------|
| **Claude Code** | `.claude/brain/` | 在 `CLAUDE.md` 中添加 `Read .claude/brain/ACTIVATE.md first` |
| **Cursor** | `.cursor/brain/` | 在 `.cursor/rules/mindkit.mdc` 中引用 |
| **WorkBuddy** | `.workbuddy/brain/` | 使用 Skill 触发 |
| **任何 LLM** | 任意位置 | 告诉它："先读 brain/ACTIVATE.md" |

### 2. 添加你的域

1. 复制 `brain/domains/_TEMPLATE.md` → `brain/domains/your_domain.md`
2. 填写关键词和核心知识
3. 将域定义添加到 `brain/FOCUS.md`

### 3. 完成

你的 AI 现在有了：
- 域特定聚焦（提到你的关键词 → 相关知识激活）
- 思维工具（说"用第一性原理" → 结构化分析）
- LTP增强直觉（重复模式 → 反应更快）
- 情景记忆索引（近期经历权重更高）
- 安全护栏（破坏性操作必须确认）

> 📖 详见 [TUTORIAL.md](TUTORIAL.md) 获取详细使用教程。

---

## 单文件版

如果你使用 ChatGPT、Gemini 或任何不支持文件访问的 LLM：

1. 打开 `mindkit-single.md`（包含在本仓库中）
2. 将其内容复制到 AI 的"自定义指令"或"系统提示词"
3. 完成 — AI 从文本中理解框架

---

## 架构

```
brain/
├── ACTIVATE.md       ⭐ 入口 — AI 首先读取
├── FOCUS.md          🎯 注意力引擎 + 域定义
├── EPISODES.md       📋 情景缓冲区 — 每日经历索引
├── INTUITION.md      ⚡ 直觉规则，LTP强化
├── THINKKIT.md       🔧 思维工具（16种方法）
├── META.md           🛡️ 安全护栏
└── domains/          📦 项目域知识
    ├── _TEMPLATE.md
    └── example_*.md
```

**加载策略**：ACTIVATE.md 是唯一必读文件。其余按需加载。

---

## 兼容性

| LLM | 最佳方式 | 备注 |
|-----|---------|------|
| Claude | 自然语言协议 | 最擅长隐式上下文 |
| GPT-4 | 结构化 YAML/表格 | 偏好显式指令 |
| Gemini | 结构化格式 | 长上下文优势 |
| Qwen | 结构化 + 中文 | 中文原生 |
| DeepSeek | 简洁结构化 | 清晰的推理链 |

---

## 进阶模式（可选）

```bash
pip install -r tools/requirements.txt

# 从模板生成新域
python tools/domain_generator.py --name "我的项目" --keywords "代码,开发,api"

# 验证 brain/ 配置
python tools/validator.py

# 在个人版和OSS版之间同步
python tools/sync_manager.py --personal /path/to/project --direction pull
```

详见 [docs/advanced-mode.md](docs/advanced-mode.md)。

---

## 贡献

欢迎贡献！详见[贡献指南](docs/contributing.md)。

我们特别需要：
- 🌍 翻译
- 📦 新域模板
- 🔧 工具改进
- 📊 真实使用案例

---

## 许可证

MIT License — 随便用。

---

*MindKit：因为"想想看"在你有思考工具的时候效果更好。*
