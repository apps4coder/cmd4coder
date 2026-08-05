---
{
  "cmd_name": "cline",
  "cmd_category": "AI基础设施/AI编程",
  "cmd_dimension": "AI编程",
  "cmd_install": "code --install-extension saoudrizwan.claude-dev",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "aider",
    "continue-dev",
    "goose"
  ],
  "cmd_tags": [
    "agent",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/ai-coding.yaml"
}
---

# cline

> Cline (前Claude Dev) VS Code自主编程Agent，可读写文件、执行命令、调用MCP工具，逐步征求确认

## 安装

```bash
code --install-extension saoudrizwan.claude-dev
```

## 用法

```
code --install-extension saoudrizwan.claude-dev
```

## 参数

| Flag | Description |
|------|-------------|
| `Plan/Act模式` | 先规划后执行的双模式切换 |
| `MCP服务器` | 通过Model Context Protocol扩展工具 |
| `Checkpoints` | 每步快照，支持回滚文件变更 |

## 示例

### 示例 1: 安装Cline扩展

```bash
code --install-extension saoudrizwan.claude-dev
```

### 示例 2: 以规划优先方式执行多文件任务

```bash
在侧边栏输入任务，选择Plan模式先生成方案
```

## 关联命令

- [[aider|aider]]
- [[continue-dev|continue-dev]]
- [[goose|goose]]

## 风险提示

> ⚠️ **HIGH**: 可自主执行shell命令与写文件，需开启命令确认，避免在生产仓库直接auto-approve

> ⚠️ **MEDIUM**: 通过MCP连接第三方工具时，代码与上下文会发送至外部LLM，敏感仓库需评估数据外泄与合规风险

## 参考链接

- [https://github.com/cline/cline](https://github.com/cline/cline)

## 最佳实践

[[bp-cline|cline 生产环境最佳实践]]

## 所属维度

[[AI编程-MOC|AI基础设施/AI编程]]
