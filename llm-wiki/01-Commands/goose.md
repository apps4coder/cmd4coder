---
{
  "cmd_name": "goose",
  "cmd_category": "AI基础设施/AI编程",
  "cmd_dimension": "AI编程",
  "cmd_install": "curl -fsSL https://github.com/block/goose/releases/download/stable/download_cli.sh | bash",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "aider",
    "cline",
    "openhands"
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

# goose

> Goose (Block开源) 本地命令行AI Agent，可自主完成编码/调试/重构，支持多LLM与MCP扩展

## 安装

```bash
curl -fsSL https://github.com/block/goose/releases/download/stable/download_cli.sh | bash
```

## 用法

```
goose [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `session` | 启动或恢复交互会话 |
| `run` | 非交互式执行一个任务指令 |
| `configure` | 配置LLM provider与扩展 |
| `--with-extension` | 临时启用指定MCP扩展 |

## 示例

### 示例 1: 交互式配置model provider与API密钥

```bash
goose configure
```

### 示例 2: 启动一个交互式编码会话

```bash
goose session
```

### 示例 3: 非交互式执行单一编码任务

```bash
goose run -t 'add unit tests for utils.py'
```

## 关联命令

- [[aider|aider]]
- [[cline|cline]]
- [[openhands|openhands]]

## 风险提示

> ⚠️ **HIGH**: Agent可执行本地命令与修改文件，建议在隔离目录或容器中运行

> ⚠️ **MEDIUM**: 非交互式 goose run 会自动批准操作，误用可能删改重要文件，生产环境须限制工作目录与权限

## 参考链接

- [https://block.github.io/goose/](https://block.github.io/goose/)

## 最佳实践

[[bp-goose|goose 生产环境最佳实践]]

## 所属维度

[[AI编程-MOC|AI基础设施/AI编程]]
