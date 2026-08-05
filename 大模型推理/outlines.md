---
{
  "cmd_name": "outlines",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "pip install outlines",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "instructor",
    "guidance",
    "langchain"
  ],
  "cmd_tags": [
    "inference",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/llm-inference.yaml"
}
---

# outlines

> LLM结构化生成库，强制模型输出JSON/Regex格式

## 安装

```bash
pip install outlines
```

## 用法

```
python -c "import outlines; ..."
```

## 示例

### 示例 1: 加载模型

```bash
python -c "import outlines; model = outlines.models.transformers('gpt2')"
```

### 示例 2: 生成JSON格式输出

```bash
python -c "import outlines; generator = outlines.generate.json(model, schema)"
```

## 关联命令

- [[instructor|instructor]]
- [[guidance|guidance]]
- [[langchain|langchain]]

## 风险提示

> ⚠️ **LOW**: 命令风险较低，执行前请阅读文档并确认参数。

## 参考链接

- [https://dottxt-ai.github.io/outlines/](https://dottxt-ai.github.io/outlines/)
- [https://github.com/dottxt-ai/outlines](https://github.com/dottxt-ai/outlines)

## 最佳实践

[[bp-outlines|outlines 生产环境最佳实践]]

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
