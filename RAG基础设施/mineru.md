---
{
  "cmd_name": "mineru",
  "cmd_category": "AI基础设施/RAG基础设施",
  "cmd_dimension": "RAG基础设施",
  "cmd_install": "pip install mineru[core]",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "marker",
    "docling",
    "unstructured"
  ],
  "cmd_tags": [
    "rag",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/rag-infra.yaml"
}
---

# mineru

> MinerU (OpenDataLab开源) PDF深度解析CLI，基于版面分析+公式识别，中文文档效果突出

## 安装

```bash
pip install mineru[core]
```

## 用法

```
mineru -p <input.pdf> -o <output_dir> [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-p, --path` | 输入PDF/图片路径 |
| `-o, --output` | 输出目录 |
| `-m, --method` | 解析方法 (auto, txt, ocr) |
| `-l, --lang` | 指定文档语言提升OCR精度 (ch, en) |

## 示例

### 示例 1: 自动判断文本层/OCR解析论文为Markdown

```bash
mineru -p paper.pdf -o ./output -m auto
```

### 示例 2: 对中文扫描件强制OCR解析

```bash
mineru -p scan.pdf -o ./output -m ocr -l ch
```

## 关联命令

- [[marker|marker]]
- [[docling|docling]]
- [[unstructured|unstructured]]

## 风险提示

> ⚠️ **MEDIUM**: 首次运行下载模型权重约数GB，GPU模式需正确配置CUDA

## 参考链接

- [https://github.com/opendatalab/MinerU](https://github.com/opendatalab/MinerU)

## 所属维度

[[RAG基础设施-MOC|AI基础设施/RAG基础设施]]
