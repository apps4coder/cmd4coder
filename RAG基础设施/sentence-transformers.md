---
{
  "cmd_name": "sentence-transformers",
  "cmd_category": "AI基础设施/RAG基础设施",
  "cmd_dimension": "RAG基础设施",
  "cmd_install": "pip install sentence-transformers",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "fastembed",
    "rerankers"
  ],
  "cmd_tags": [
    "rag",
    "vector-db",
    "quantization",
    "fine-tuning",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/rag-infra.yaml"
}
---

# sentence-transformers

> Sentence-Transformers 文本向量化事实标准库，支持embedding、rerank与对比学习微调

## 安装

```bash
pip install sentence-transformers
```

## 用法

```
python embed.py (使用sentence_transformers库)
```

## 参数

| Flag | Description |
|------|-------------|
| `SentenceTransformer` | 加载embedding模型 |
| `CrossEncoder` | 加载交叉编码器用于精排 |
| `encode` | 批量编码文本为向量 (batch_size, normalize_embeddings) |
| `similarity` | 计算向量相似度矩阵 |

## 示例

### 示例 1: 用BGE-M3生成归一化embedding

```bash
python -c "from sentence_transformers import SentenceTransformer; model = SentenceTransformer('BAAI/bge-m3'); emb = model.encode(['你好世界'], normalize_embeddings=True)"
```

### 示例 2: 用BGE reranker对候选文档精排打分

```bash
python -c "from sentence_transformers import CrossEncoder; ce = CrossEncoder('BAAI/bge-reranker-v2-m3'); scores = ce.predict([('query', 'doc1'), ('query', 'doc2')])"
```

## 关联命令

- [[fastembed|fastembed]]
- [[rerankers|rerankers]]

## 风险提示

> ⚠️ **LOW**: 首次运行自动从HuggingFace下载模型，离线环境需预置缓存

## 参考链接

- [https://www.sbert.net/](https://www.sbert.net/)

## 所属维度

[[RAG基础设施-MOC|AI基础设施/RAG基础设施]]
