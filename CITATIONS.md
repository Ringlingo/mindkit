# MindKit 参考文献与致谢

> 本文档列出 MindKit 开发过程中引用的学术论文、书籍和其他资源。

---

## 核心学术来源

### 1. 工作记忆模型 (Working Memory Model)

**来源**: Baddeley, A. D., & Hitch, G. (1974). Working Memory. In G. H. Bower (Ed.), Psychology of Learning and Motivation (Vol. 8, pp. 47-89). Academic Press.

**关键贡献**:
- 中央执行器 (Central Executive)：注意力管理和任务协调
- 语音环路 (Phonological Loop)：口头/书面语言信息处理
- 视觉空间模板 (Visuospatial Sketchpad)：视觉图像和空间信息处理
- 情景缓冲区 (Episodic Buffer, 2000年更新)：整合多源信息形成统一情景

**对 MindKit 的影响**:
- EPISODES.md 的设计直接对应情景缓冲区概念
- 工作记忆有限容量 → Token 预算指南
- 多组件分工 → 模块化架构

**参考链接**: https://www.simplypsychology.org/working-memory.html

---

### 2. 记忆宫殿方法 (Method of Loci)

**来源**:
- Dresler, M., et al. (2017). Mnemonic Training Reshapes Brain Networks to Support Superior Memory. *Neuron*, 93(5), 1227-1235.
- Wikipedia: Method of Loci

**关键贡献**:
- 空间结构作为记忆检索脚手架
- 6周训练可使普通人达到记忆竞技选手水平
- 空间导航网络与记忆编码网络的功能连接协调

**对 MindKit 的影响**:
- 情景缓冲区的空间索引概念
- "按位置检索"的思路
- 近因效应（最近使用优先）的心理学基础

**参考链接**: https://cognitivetrain.com/method-of-loci/

---

### 3. 长期记忆与 AI 自我进化

**来源**: Jiang, X., et al. (2024). Long Term Memory: The Foundation of AI Self-Evolution. *arXiv:2410.15665*.

**关键贡献**:
- LTM 支撑推理过程中的 AI 自我进化
- 皮层柱状组织启发 AI 认知架构
- 多智能体框架 OMNE 在 GAIA 基准测试中获第一

**对 MindKit 的影响**:
- 确认长期记忆对 AI 能力的重要性
- LTP (长时程增强) 机制 → INTUITION.md 的强度更新规则
- "经验积累→能力提升"的框架设计

**参考链接**: https://arxiv.org/abs/2410.15665

---

### 4. 人脑记忆系统分类

**来源**: Rolls, E. T. (2024). Memory systems in the brain and generative AI. *Oxcns.org*.

**关键贡献**:
- 语义记忆 (Semantic Memory)：事实和概念
- 情景记忆 (Episodic Memory)：个人经历
- 程序记忆 (Procedural Memory)：技能和习惯

**对 MindKit 的影响**:
- domains/*.md → 语义记忆（事实知识）
- EPISODES.md → 情景记忆（经历索引）
- INTUITION.md → 程序记忆（自动化反应）

**参考链接**: https://www.oxcns.org/papers/684%20Rolls%202024%20Memory%20systems%20in%20the%20brain%20and%20generative%20AI%20.pdf

---

### 5. 海马体记忆巩固机制

**来源**:
- McClelland, J. L., McNaughton, B. L., & O'Reilly, R. C. (1995). Why there are complementary learning systems in the hippocampus and neocortex. *Psychological Review*, 102(3), 419-457.
- Atkinson, R. C., & Shiffrin, R. M. (1968). Human memory: A proposed system and its control processes. *Psychology of Learning and Motivation*, 2, 89-195.

**关键贡献**:
- 海马体-新皮层双系统记忆巩固
- 瞬时记忆→短期记忆→长期记忆的分层
- 重复激活→突触强化 (LTP)

**对 MindKit 的影响**:
- 记忆分层架构设计
- LTP 强化机制（使用次数→触发阈值）
- 巩固和检索的分离

---

### 6. 认知心理学与注意力

**来源**: Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.

**关键贡献**:
- 系统1（快速直觉）和系统2（慢速分析）
- 注意力作为有限资源
- 认知偏误的系统性整理

**对 MindKit 的影响**:
- 注意力引擎的设计（聚焦 vs 抑制）
- 思维工具分类（分析型 vs 创造型）
- 安全护栏的必要性和设计

---

## 致谢

### 开源项目参考

- **MemPalace**: https://zhanghandong.github.io/mempalace-book/
  - 记忆宫殿的 AI 实现参考
  - Wing/Hall/Room 分层结构的思考

- **Mem0**: https://github.com/mem0ai/mem0
  - 个人 AI 记忆系统的设计参考

- **Letta**: https://github.com/letta/letta
  - LLM 记忆管理的架构参考

---

## 声明

MindKit 是一个**受脑科学启发的认知框架**，但它：

1. **不是神经科学的精确复制** —— 我们借鉴原理，不是复制机制
2. **不是声称 AI 具有意识** —— 框架提供结构，不是赋予生命
3. **不是唯一正确的方案** —— 存在许多有效的设计选择

所有引用的脑科学研究都有其局限性，MindKit 的设计是对这些原理的**工程化应用**，在某些地方可能过度简化或需要调整以适应实际需求。

如果你发现设计上的问题或有改进建议，欢迎提交 Issue 或 PR。

---

*最后更新: 2026-04-19*
