---
{
  "cmd_name": "rerankers",
  "cmd_category": "AI基础设施/RAG基础设施",
  "cmd_dimension": "RAG基础设施",
  "cmd_install": "pip install rerankers[all]",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "sentence-transformers",
    "ragas"
  ],
  "cmd_tags": [
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

# rerankers

> Rerankers 统一重排接口库，一套API切换CrossEncoder/ColBERT/Cohere/Jina等精排后端

## 安装

```bash
pip install rerankers[all]
```

## 用法

```
python rerank.py (使用rerankers库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Reranker` | 统一入口，按模型名自动选择后端 |
| `rank` | 对query+docs执行重排 |
| `model_type` | 显式指定后端 (cross-encoder, colbert, api) |

## 示例

### 示例 1: 本地CrossEncoder重排检索结果

```bash
python -c "from rerankers import Reranker; r = Reranker('BAAI/bge-reranker-v2-m3'); results = r.rank(query='什么是RAG', docs=docs)"
```

### 示例 2: 切换到Cohere API后端，代码无需改动

```bash
python -c "from rerankers import Reranker; r = Reranker('cohere', api_key='...'); results = r.rank(query=q, docs=docs)"
```

## 关联命令

- [[sentence-transformers|sentence-transformers]]
- [[ragas|ragas]]

## 风险提示

> ⚠️ **LOW**: API后端会将文档内容发送至第三方服务，敏感数据需用本地后端

## 参考链接

- [https://github.com/AnswerDotAI/rerankers](https://github.com/AnswerDotAI/rerankers)

## 最佳实践

[[bp-rerankers|rerankers 生产环境最佳实践]]

## 所属维度

[[RAG基础设施-MOC|AI基础设施/RAG基础设施]]
