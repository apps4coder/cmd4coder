---
{
  "cmd_name": "chonkie",
  "cmd_category": "AI基础设施/RAG基础设施",
  "cmd_dimension": "RAG基础设施",
  "cmd_install": "pip install chonkie",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "unstructured",
    "fastembed"
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

# chonkie

> Chonkie 轻量高性能文本分块库，支持token/sentence/semantic/late等多种chunking策略

## 安装

```bash
pip install chonkie
```

## 用法

```
python chunk.py (使用chonkie库)
```

## 参数

| Flag | Description |
|------|-------------|
| `TokenChunker` | 按token数定长分块 |
| `SentenceChunker` | 按句子边界分块 |
| `SemanticChunker` | 按语义相似度自适应分块 |
| `RecursiveChunker` | 按层级分隔符递归分块 |

## 示例

### 示例 1: 递归分块，每块最大512 token

```bash
python -c "from chonkie import RecursiveChunker; chunker = RecursiveChunker(chunk_size=512); chunks = chunker('long text...')"
```

### 示例 2: 语义分块，相似度阈值0.5处断开

```bash
python -c "from chonkie import SemanticChunker; chunker = SemanticChunker(embedding_model='minishlab/potion-base-8M', threshold=0.5); chunks = chunker(text)"
```

## 关联命令

- [[unstructured|unstructured]]
- [[fastembed|fastembed]]

## 风险提示

> ⚠️ **LOW**: 只读处理，无副作用

## 参考链接

- [https://github.com/chonkie-inc/chonkie](https://github.com/chonkie-inc/chonkie)

## 所属维度

[[RAG基础设施-MOC|AI基础设施/RAG基础设施]]
