---
{
  "cmd_name": "mistral",
  "cmd_category": "AI基础设施/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "pip install mistralai 或参考官方",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "openai",
    "cohere"
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

# mistral

> Mistral AI CLI

## 安装

```bash
pip install mistralai 或参考官方
```

## 用法

```
mistral [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `chat` |  |
| `list` | models |

## 示例

### 示例 1: 聊天

```bash
mistral chat --message 'Explain RAG'
```

### 示例 2: 列出模型

```bash
mistral list-models
```

## 关联命令

- [[openai|openai]]
- [[cohere|cohere]]

## 风险提示

> ⚠️ **LOW**: 命令风险较低，执行前请阅读文档并确认参数。

## 参考链接

- [https://docs.mistral.ai/](https://docs.mistral.ai/)
- [https://github.com/mistralai/client-python](https://github.com/mistralai/client-python)

## 最佳实践

[[bp-mistral|mistral 生产环境最佳实践]]

## 所属维度

[[扩展命令-MOC|AI基础设施/扩展命令]]
