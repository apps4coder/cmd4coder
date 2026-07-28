---
{
  "cmd_name": "ragas",
  "cmd_category": "AI基础设施/RAG基础设施",
  "cmd_dimension": "RAG基础设施",
  "cmd_install": "pip install ragas",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "unstructured",
    "sentence-transformers"
  ],
  "cmd_tags": [
    "rag",
    "quantization",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/rag-infra.yaml"
}
---

# ragas

> Ragas RAG评估框架，量化faithfulness/answer_relevancy/context_precision等核心指标

## 安装

```bash
pip install ragas
```

## 用法

```
python evaluate.py (使用ragas库)
```

## 参数

| Flag | Description |
|------|-------------|
| `evaluate` | 对数据集执行多指标评估 |
| `faithfulness` | 忠实度：答案是否忠于检索上下文 |
| `answer_relevancy` | 答案与问题的相关性 |
| `context_precision` | 检索上下文的精确度 |
| `TestsetGenerator` | 从文档自动合成评估测试集 |

## 示例

### 示例 1: 评估RAG管道的忠实度与答案相关性

```bash
python -c "from ragas import evaluate; from ragas.metrics import faithfulness, answer_relevancy; result = evaluate(dataset, metrics=[faithfulness, answer_relevancy])"
```

### 示例 2: 从文档集自动生成50条评估样本

```bash
python -c "from ragas.testset import TestsetGenerator; testset = TestsetGenerator.from_langchain(llm).generate_with_langchain_docs(docs, testset_size=50)"
```

## 关联命令

- [[unstructured|unstructured]]
- [[sentence-transformers|sentence-transformers]]

## 风险提示

> ⚠️ **MEDIUM**: 评估依赖LLM作为judge，大数据集会产生可观API费用

## 参考链接

- [https://docs.ragas.io/](https://docs.ragas.io/)

## 所属维度

[[RAG基础设施-MOC|AI基础设施/RAG基础设施]]
