# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

纯静态 HTML/CSS/JS（无构建步骤），产出位于仓库内 `GTM/` 文件夹，浏览器直接打开即可预览，未来可直接部署到 GitHub Pages。

## Users

四类受众，兼顾：
- AI Agent / Coding Agent 开发者：为 RAG 与工具链寻找高质量、结构化的命令行语料。
- 运维与平台工程师（SRE/DevOps）：沉淀命令风险与生产最佳实践，用于排障。
- 泛开发者：查阅命令用法、避坑、学习。
- 企业与数据合作方：评估将语料集成为私有知识库或授权合作。

## Product Purpose

一个以 Markdown 为核心的命令行语料数据库：持续沉淀每一条命令行的内涵外延、使用方式与风险，最终支撑智能体问答与问题排查。成功 = 语料被真实用于 Agent 检索与排障，且社区持续贡献命令条目。

## Positioning

YAML 单一数据源 → 自动生成带双向链接的 Markdown 语料 → CLI 检索/校验，三层一致、机器可读且人类可读。每条命令同时沉淀「内涵外延 + 生产最佳实践 + 风险」三件套，这是普通 man page 与命令速查站都不具备的结构。100 领域 · 1137 命令页 · 741 最佳实践页是当前真实规模。

## Operating Context

- 语料在 Git 仓库中，以「中文领域文件夹 / 命令.md」二层扁平结构组织。
- 配套 `cmd4coder` Go CLI：categories / search / show 子命令，另有 validator 校验数据源。
- 整个仓库可作为 Obsidian Vault 打开，利用双向链接可视化浏览。
- 内容生成链路：编辑 `tools/cmd/data/*.yaml` → validator 校验 → `convert_to_wiki.py` 重新生成 md。

## Capabilities and Constraints

- 能力：命令检索、分类浏览、详情查看、数据校验、双向链接浏览。
- 数据权威源：`tools/cmd/data/` 下 129 个 YAML 文件；根目录 2136 个 Markdown 为生成产物。
- 许可证：MIT。语言：语料为中文。
- 未定事实：是否提供在线托管站点、企业授权的商业模式均未决定，页面不虚构。

## Evidence on Hand

- INDEX.md：100 领域 · 1137 命令页 · 741 最佳实践页（权威计数）。
- 真实领域示例：大模型训练（deepspeed/accelerate）、大模型推理（vllm/sglang）、K8s 全生态、Java诊断、Linux核心、Git、Docker、Terraform 等。
- 真实命令示例可直接从根目录领域文件夹引用（如 `大模型训练/deepspeed.md`、`bp-deepspeed.md`）。
- 无客户见证、无基准测试、无定价——页面不得虚构此类声明。

## Product Principles

1. 语料质量优先于数量展示：页面要用真实结构示例（含风险与最佳实践）证明质量，而非只报数字。
2. 三层一致性（YAML 源 → Markdown → CLI）是机制卖点，必须以可视化方式演示。
3. 面向 Agent 的可消费性是第一受众价值：强调机器可读、可嵌入、可校验。
4. 开源 + MIT + 可贡献：所有转化路径都真实存在于仓库。
