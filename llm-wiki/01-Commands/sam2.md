---
{
  "cmd_name": "sam2",
  "cmd_category": "AI基础设施/多模态",
  "cmd_dimension": "多模态",
  "cmd_install": "pip install git+https://github.com/facebookresearch/sam2.git",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "clip",
    "comfyui"
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

# sam2

> SAM 2 (Meta) 图像与视频通用分割模型，支持提示式分割与视频对象追踪

## 安装

```bash
pip install git+https://github.com/facebookresearch/sam2.git
```

## 用法

```
python segment.py (使用sam2库)
```

## 参数

| Flag | Description |
|------|-------------|
| `SAM2ImagePredictor` | 图像分割预测器 |
| `SAM2VideoPredictor` | 视频分割与追踪预测器 |
| `build_sam2` | 加载指定规格模型权重 |

## 示例

### 示例 1: 加载SAM2图像分割模型

```bash
python -c "from sam2.sam2_image_predictor import SAM2ImagePredictor; p = SAM2ImagePredictor.from_pretrained('facebook/sam2-hiera-large')"
```

### 示例 2: 初始化视频分割器进行对象追踪

```bash
python -c "from sam2.build_sam import build_sam2_video_predictor; predictor = build_sam2_video_predictor(cfg, ckpt); state = predictor.init_state('video/')"
```

## 关联命令

- [[clip|clip]]
- [[comfyui|comfyui]]

## 风险提示

> ⚠️ **LOW**: 模型权重较大，视频推理需GPU支持

## 参考链接

- [https://github.com/facebookresearch/sam2](https://github.com/facebookresearch/sam2)

## 最佳实践

[[bp-sam2|sam2 生产环境最佳实践]]

## 所属维度

[[多模态-MOC|AI基础设施/多模态]]
