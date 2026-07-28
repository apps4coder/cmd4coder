---
{
  "cmd_name": "fastembed",
  "cmd_category": "AI基础设施/RAG基础设施",
  "cmd_dimension": "RAG基础设施",
  "cmd_install": "pip install fastembed",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "sentence-transformers"
  ],
  "cmd_tags": [
    "inference",
    "rag",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/rag-infra.yaml"
}
---

# fastembed

> FastEmbed (Qdrant开源) 轻量级ONNX embedding库，无PyTorch依赖，CPU推理快5-10倍

## 安装

```bash
pip install fastembed
```

## 用法

```
python embed.py (使用fastembed库)
```

## 参数

| Flag | Description |
|------|-------------|
| `TextEmbedding` | 稠密向量模型 |
| `SparseTextEmbedding` | 稀疏向量模型 (BM42/SPLADE) |
| `LateInteractionTextEmbedding` | ColBERT延迟交互模型 |

## 示例

### 示例 1: CPU上快速生成稠密向量

```bash
python -c "from fastembed import TextEmbedding; model = TextEmbedding('BAAI/bge-small-en-v1.5'); embs = list(model.embed(['hello world']))"
```

### 示例 2: 生成BM42稀疏向量用于混合检索

```bash
python -c "from fastembed import SparseTextEmbedding; model = SparseTextEmbedding('Qdrant/bm42-all-minilm-l6-v2-attentions'); embs = list(model.embed(['hello world']))"
```

## 关联命令

- [[sentence-transformers|sentence-transformers]]

## 风险提示

> ⚠️ **LOW**: 仅支持已转换为ONNX的模型列表，自定义模型需自行转换

## 参考链接

- [https://qdrant.github.io/fastembed/](https://qdrant.github.io/fastembed/)

## 所属维度

[[RAG基础设施-MOC|AI基础设施/RAG基础设施]]
