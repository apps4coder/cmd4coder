---
{
  "cmd_name": "olive",
  "cmd_category": "AI基础设施/AI编译器",
  "cmd_dimension": "AI编译器",
  "cmd_install": "pip install olive-ai",
  "cmd_platforms": [
    "linux",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "onnx-optimizer",
    "trtexec"
  ],
  "cmd_tags": [
    "compiler",
    "quantization",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/ai-compiler.yaml"
}
---

# olive

> Olive (微软开源) 硬件感知模型优化工具链，自动搜索量化/转换/图优化组合，产出ONNX

## 安装

```bash
pip install olive-ai
```

## 用法

```
olive run --config <config.json>
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 执行优化工作流 |
| `--config` | 指定优化pass与目标硬件配置 |
| `auto-opt` | 自动优化模式，无需手写配置 |

## 示例

### 示例 1: 自动为GPU优化并导出Llama模型

```bash
olive auto-opt -m meta-llama/Llama-3.2-1B -o ./optimized --device gpu
```

### 示例 2: 按配置执行量化+转换流水线

```bash
olive run --config quantize_config.json
```

## 关联命令

- [[onnx-optimizer|onnx-optimizer]]
- [[trtexec|trtexec]]

## 风险提示

> ⚠️ **MEDIUM**: 自动搜索耗时且占用大量显存，量化后需验证精度损失

## 参考链接

- [https://microsoft.github.io/Olive/](https://microsoft.github.io/Olive/)

## 最佳实践

[[bp-olive|olive 生产环境最佳实践]]

## 所属维度

[[AI编译器-MOC|AI基础设施/AI编译器]]
