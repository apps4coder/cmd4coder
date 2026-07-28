---
{
  "cmd_name": "ncnn",
  "cmd_category": "AI基础设施/边缘AI",
  "cmd_dimension": "边缘AI",
  "cmd_install": "git clone https://github.com/Tencent/ncnn && cmake构建",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "tflite",
    "paddle-lite"
  ],
  "cmd_tags": [
    "inference",
    "edge",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/edge-ai.yaml"
}
---

# ncnn

> ncnn (腾讯开源) 面向手机端的高性能神经网络推理框架，无第三方依赖，ARM NEON深度优化

## 安装

```bash
git clone https://github.com/Tencent/ncnn && cmake构建
```

## 用法

```
onnx2ncnn model.onnx model.param model.bin
```

## 参数

| Flag | Description |
|------|-------------|
| `onnx2ncnn` | 将ONNX模型转为ncnn格式 |
| `ncnnoptimize` | 图优化与fp16压缩 |
| `ncnn2int8` | INT8量化工具 |

## 示例

### 示例 1: 将ONNX模型转换为ncnn格式

```bash
onnx2ncnn model.onnx model.param model.bin
```

### 示例 2: 对模型执行图优化并转fp16

```bash
ncnnoptimize model.param model.bin opt.param opt.bin 65536
```

## 关联命令

- [[tflite|tflite]]
- [[paddle-lite|paddle-lite]]

## 风险提示

> ⚠️ **LOW**: INT8量化后需在目标机型上验证精度与延迟

## 参考链接

- [https://github.com/Tencent/ncnn](https://github.com/Tencent/ncnn)

## 所属维度

[[边缘AI-MOC|AI基础设施/边缘AI]]
