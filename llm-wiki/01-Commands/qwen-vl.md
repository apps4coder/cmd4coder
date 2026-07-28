---
{
  "cmd_name": "qwen-vl",
  "cmd_category": "AI基础设施/多模态",
  "cmd_dimension": "多模态",
  "cmd_install": "pip install transformers qwen-vl-utils",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "llava",
    "clip"
  ],
  "cmd_tags": [
    "multimodal",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/multimodal.yaml"
}
---

# qwen-vl

> Qwen-VL (阿里巴巴) 开源视觉语言模型，支持图像/视频理解、OCR与多图对话

## 安装

```bash
pip install transformers qwen-vl-utils
```

## 用法

```
python vl_infer.py (使用transformers加载Qwen-VL)
```

## 参数

| Flag | Description |
|------|-------------|
| `Qwen2VLForConditionalGeneration` | 多模态生成模型类 |
| `process_vision_info` | 预处理图像/视频输入 |
| `min_pixels/max_pixels` | 控制图像分辨率以平衡显存与精度 |

## 示例

### 示例 1: 加载Qwen2-VL-7B多模态模型

```bash
python -c "from transformers import Qwen2VLForConditionalGeneration; m = Qwen2VLForConditionalGeneration.from_pretrained('Qwen/Qwen2-VL-7B-Instruct')"
```

### 示例 2: 预处理图像/视频输入以构造多模态prompt

```bash
python -c "from qwen_vl_utils import process_vision_info; image_inputs, video_inputs = process_vision_info(messages)"
```

## 关联命令

- [[llava|llava]]
- [[clip|clip]]

## 风险提示

> ⚠️ **LOW**: 高分辨率图像会显著增加显存占用，需调优pixels参数

## 参考链接

- [https://github.com/QwenLM/Qwen2-VL](https://github.com/QwenLM/Qwen2-VL)

## 所属维度

[[多模态-MOC|AI基础设施/多模态]]
