---
{
  "cmd_name": "torch-compile",
  "cmd_category": "AI基础设施/AI编译器",
  "cmd_dimension": "AI编译器",
  "cmd_install": "PyTorch 2.0+ 内置 (pip install torch)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "onnx-optimizer",
    "tvmc"
  ],
  "cmd_tags": [
    "compiler",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/ai-compiler.yaml"
}
---

# torch-compile

> torch.compile PyTorch原生JIT编译器，基于TorchDynamo+Inductor自动图捕获与算子融合，一行提速

## 安装

```bash
PyTorch 2.0+ 内置 (pip install torch)
```

## 用法

```
model = torch.compile(model, mode='...', backend='inductor')
```

## 参数

| Flag | Description |
|------|-------------|
| `mode` | 编译模式 (default, reduce-overhead, max-autotune) |
| `backend` | 后端 (inductor, cudagraphs, onnxrt, tensorrt) |
| `fullgraph` | 强制全图捕获，禁止graph break |
| `dynamic` | 支持动态shape避免重复编译 |

## 示例

### 示例 1: 以最大自动调优模式编译模型

```bash
python -c "import torch; m = torch.compile(model, mode='max-autotune')"
```

### 示例 2: 小批量推理降低Python开销（启用CUDA Graphs）

```bash
python -c "import torch; m = torch.compile(model, mode='reduce-overhead')"
```

## 关联命令

- [[onnx-optimizer|onnx-optimizer]]
- [[tvmc|tvmc]]

## 风险提示

> ⚠️ **LOW**: 首次编译耗时较长；频繁变化的shape会触发重编译拖慢速度

## 参考链接

- [https://pytorch.org/docs/stable/generated/torch.compile.html](https://pytorch.org/docs/stable/generated/torch.compile.html)

## 所属维度

[[AI编译器-MOC|AI基础设施/AI编译器]]
