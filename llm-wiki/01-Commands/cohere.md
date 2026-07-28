---
{
  "cmd_name": "cohere",
  "cmd_category": "AI基础设施/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "pip install cohere 或参考官方 SDK",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "openai",
    "mistral"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/more.yaml"
}
---

# cohere

> Cohere 命令行工具

## 安装

```bash
pip install cohere 或参考官方 SDK
```

## 用法

```
cohere [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `chat` |  |
| `embed` |  |
| `classify` |  |

## 示例

### 示例 1: 聊天

```bash
cohere chat --message 'Hello'
```

### 示例 2: 生成向量

```bash
cohere embed --texts 'hello world'
```

## 关联命令

- [[openai|openai]]
- [[mistral|mistral]]

## 风险提示

> ⚠️ **LOW**: 命令风险较低，执行前请阅读文档并确认参数。

## 所属维度

[[扩展命令-MOC|AI基础设施/扩展命令]]
