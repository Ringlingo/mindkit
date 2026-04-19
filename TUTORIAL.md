# MindKit 完整使用教程

> 本教程面向希望将 MindKit 集成到日常工作流程的 AI 助手开发者和用户。
> 涵盖从零开始的完整设置流程，以及如何高效使用每个模块。

---

## 目录

1. [概念理解](#1-概念理解)
2. [快速开始](#2-快速开始)
3. [域管理](#3-域管理)
4. [直觉规则](#4-直觉规则)
5. [情景缓冲区](#5-情景缓冲区)
6. [思维工具](#6-思维工具)
7. [高级配置](#7-高级配置)
8. [最佳实践](#8-最佳实践)

---

## 1. 概念理解

### MindKit 是什么

MindKit 是一个**认知框架**，不是插件或数据库。它通过组织良好的 Markdown 文件，告诉 AI 如何：

- **聚焦**：遇到特定话题时，自动加载相关知识
- **思考**：使用结构化思维工具分析问题
- **记忆**：通过直觉规则和情景缓冲区记住重要模式
- **安全**：对高危操作自动触发确认机制

### 四大核心模块

```
┌─────────────────────────────────────────────────────┐
│                    MindKit                       │
├─────────────────────────────────────────────────────┤
│  🎯 Focus Engine     →  聚焦相关域，抑制干扰       │
│  ⚡ Intuition Rules  →  LTP强化的快速反应规则       │
│  📋 Episodic Buffer  →  每日经历的索引             │
│  🛡️ Safety          →  不可逾越的安全线            │
└─────────────────────────────────────────────────────┘
```

### 与脑科学的对应关系

| MindKit 模块 | 脑科学对应 | 功能 |
|----------------|-----------|------|
| FOCUS.md | 中央执行器 | 注意力选择与资源分配 |
| INTUITION.md | 程序记忆 | 经过练习强化的自动化反应 |
| EPISODES.md | 情景记忆 | 每日经历的情境索引 |
| THINKKIT.md | 前额叶执行功能 | 结构化问题解决 |

---

## 2. 快速开始

### Step 1: 选择你的 AI 工具

| AI 工具 | 安装位置 | 激活方式 |
|---------|---------|---------|
| Claude Code | `.claude/brain/` | 在 `CLAUDE.md` 添加读取指令 |
| Cursor | `.cursor/brain/` | 创建 `.cursor/rules/mindkit.mdc` |
| ChatGPT/Gemini | 不需要 | 直接使用 `mindkit-single.md` |

### Step 2: 复制 brain/ 目录

```bash
# Claude Code
cp -r brain/ /path/to/your-project/.claude/brain/

# Cursor
cp -r brain/ /path/to/your-project/.cursor/brain/
```

### Step 3: 激活框架

**Claude Code**: 在 `CLAUDE.md` 添加：
```
Read .claude/brain/ACTIVATE.md first at the start of every conversation.
```

**Cursor**: 创建 `.cursor/rules/mindkit.mdc`：
```markdown
---
description: MindKit cognitive framework
globs:
alwaysApply: true
---

Read .cursor/brain/ACTIVATE.md first at the start of every conversation.
```

**ChatGPT/Gemini**: 打开 `mindkit-single.md`，复制全部内容到"自定义指令"。

### Step 4: 验证安装

启动一个新对话，说：
> "告诉我你知道哪些关于 [你的一个域关键词] 的知识"

如果 AI 引用了你域文件中的具体知识，说明安装成功。

---

## 3. 域管理

### 什么是域

域（Domain）是你的**知识边界**。每个域包含：
- 关键词（用于触发）
- 核心知识文件路径
- 用户偏好

### 创建新域

1. 复制模板：
```bash
cp brain/domains/_TEMPLATE.md brain/domains/my_domain.md
```

2. 编辑 `my_domain.md`：
```yaml
==FRAGMENT:core==

## Core Knowledge
- **项目路径**: /path/to/my/project
- **技术栈**: React, Node.js, PostgreSQL

## Key Preferences
- 喜欢模块化代码结构
- 优先考虑性能优化
- 需要详细的代码注释

==END==
```

3. 在 `FOCUS.md` 添加域定义：
```yaml
domain: my_domain
name: "My Project"
icon: "💼"
keywords: [react, node, backend, api, database]
```

### 域的触发机制

当你的输入包含某个域的关键词时，AI 会：
1. 自动加载该域的 `core` 片段
2. 优先使用该域的知识回答问题
3. 抑制不相关的域

**示例**：
```
输入: "帮我看看这个 React 组件的性能问题"
→ 触发 frontend_dev 域
→ AI 加载前端开发相关知识
```

---

## 4. 直觉规则

### 什么是直觉规则

直觉规则是**从重复经验中提炼的快速反应**。当某个模式被验证3次以上，它就变成了"直觉"——不需要思考，条件反射般触发。

### LTP 强化机制

基于神经科学的**长时程增强（LTP）**原理：

```
使用次数 ↑ → 触发阈值 ↓ → 反应更自动
```

| 使用次数 | 触发阈值 | 行为表现 |
|---------|---------|---------|
| 1-2次 | 需明确匹配 | 谨慎确认 |
| 3-5次 | 模糊匹配触发 | 开始自动 |
| 6+次 | 几乎即时 | 条件反射 |

### 添加新规则

在 `INTUITION.md` 中添加：

```yaml
- id: INT-003
  trigger: "用户说 '先不执行'"
  action: "切换分析模式，只输出方案不执行"
  strength: 0.7      # 新规则初始强度
  source: experience
  verified_count: 3  # 必须验证3次
  last_used: 2026-04-19
```

### 规则强度更新

每次成功触发后：
```
成功触发 → 累计+1 → 强度+0.02（上限1.0）
触发失败 → 强度-0.1 → 低于0.5标记为"待复核"
```

---

## 5. 情景缓冲区

### 什么是情景缓冲区

情景缓冲区记录**每日交互的关键事件**——不是知识，而是"发生了什么"。

每条记录包含：
- 日期
- 主题
- 关键事件
- 情感标记
- 相关域

### 使用示例

```yaml
episodes:

  - date: 2026-04-19
    theme: "MindKit v2.1 发布"
    key_events:
      - "新增 LTP 强化机制"
      - "新增情景缓冲区 EPISODES.md"
      - "移除过时的 PALACE.md"
    emotion: breakthrough
    domains: [mindkit, documentation]
```

### 检索优先级

检索时，**近因效应**生效：
- 最近的事件权重更高
- 超过30天自动归档

---

## 6. 思维工具

### 16 个思维工具

| 类别 | 工具 | 适用场景 |
|------|------|---------|
| 🔍 分析 | 第一性原理 | 追问本质 |
| 🔍 分析 | 费曼检验 | 能否向外行解释清 |
| 🔍 分析 | 逆向思维 | 从目标反推路径 |
| 🔍 分析 | 还原论 | 拆解到最小单元 |
| 🎨 创造 | 跨学科碰撞 | 突破思维定势 |
| 🎨 创造 | 类比迁移 | A域解法→B域 |
| 🎨 创造 | 极端假设 | 探索可能性 |
| 🎨 创造 | 否定之否定 | 重建新方案 |
| 🛡️ 验证 | 魔鬼代言人 | 主动找反例 |
| 🛡️ 验证 | 边界测试 | 极端条件检验 |
| 🛡️ 验证 | 一致性检查 | 是否自相矛盾 |
| 🛡️ 验证 | 奥卡姆剃刀 | 最简解释优先 |
| 🧭 导向 | 目标锚定 | 是否服务核心目标 |
| 🧭 导向 | 机会成本 | 选择A放弃什么 |
| 🧭 导向 | 二阶效应 | 后续影响是什么 |
| 🧭 导向 | 正向引导 | 从成功中提炼 |

### 使用方法

在对话中说：
> "用第一性原理分析这个问题"

AI 会加载第一性原理工具，进行结构化分析。

---

## 7. 高级配置

### Python 工具（可选）

```bash
pip install -r tools/requirements.txt
```

**域生成器**：
```bash
python tools/domain_generator.py --name "my_project" --keywords "code,dev,api"
```

**配置验证器**：
```bash
python tools/validator.py
```

**同步管理器**（个人版 ↔ 开源版）：
```bash
python tools/sync_manager.py --personal /path/to/personal --direction pull
```

### Token 预算

| 上下文大小 | 建议策略 |
|-----------|---------|
| 4K tokens | ACTIVATE.md + 1个域 + 直觉扫描 |
| 8K tokens | + 思维工具目录 + 1个扩散域 |
| 16K+ tokens | 全部加载 |

---

## 8. 最佳实践

### ✅ 推荐做法

1. **域关键词要具体**
   - ❌ "编程" → 太宽泛
   - ✅ "react, typescript, hooks" → 精准触发

2. **直觉规则要验证3次以上**
   - 第一次观察到：记录但不添加
   - 第二次出现：标记为待验证
   - 第三次验证：正式添加

3. **情景缓冲区要及时记录**
   - 每个重要会话结束后添加
   - 包含关键决策和成果
   - 标注情感状态

4. **域文件保持精简**
   - 只放最常用的知识
   - 深层知识用 FRAGMENT:deep
   - 按需加载，不占默认空间

### ❌ 避免做法

1. **不要过度设计域结构**
   - 5个域足够覆盖大多数需求
   - 增加太多域会导致注意力分散

2. **不要添加无法验证的直觉规则**
   - 规则必须有实际触发场景
   - 3次验证是最低标准

3. **不要让情景缓冲区变成流水账**
   - 只记录有意义的事件
   - 无关痛痒的对话不需要记录

---

## 故障排除

### AI 没有触发域
- 检查关键词是否在输入中
- 确认域定义已添加到 FOCUS.md
- 确认域文件路径正确

### 直觉规则没有生效
- 确认规则已添加到 INTUITION.md
- 检查触发条件是否与输入匹配
- 确认使用次数达到触发阈值

### 安全规则没有弹出确认
- 安全规则（HR-001~005）不可覆盖
- 如果AI跳过了确认，这是Bug，请报告

---

## 下一步

- 查看 [QUICKSTART.md](QUICKSTART.md) 获取3步快速指南
- 查看 [examples/](examples/) 目录获取各 AI 工具的具体配置
- 查看 [docs/](docs/) 目录获取高级文档

---

_使用 MindKit，让 AI 的每一次思考都更加聚焦和有效。_
