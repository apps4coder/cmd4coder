---
{
  "cmd_name": "llama.cpp",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "git clone https://github.com/ggerganov/llama.cpp && make",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ollama",
    "gguf-convert"
  ],
  "cmd_tags": [
    "inference",
    "edge",
    "quantization",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-inference.yaml"
}
---

# llama.cpp

> llama.cpp纯C/C++实现的LLM推理，支持GGUF量化，可在CPU/边缘设备运行

## 安装

```bash
git clone https://github.com/ggerganov/llama.cpp && make
```

## 用法

```
./main [OPTIONS]
```

```
./server [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-m` | GGUF模型文件路径 |
| `-n` | 生成token数量 |
| `--temp` | 采样温度(默认0.8) |
| `-ngl` | GPU加载的层数 |
| `-c` | 上下文大小 |

## 示例

### 示例 1: CPU推理运行量化模型

```bash
./main -m models/llama-3.1-8b.Q4_K_M.gguf -n 512 --temp 0.7 -p 'What is machine learning?'
```

### 示例 2: 启动HTTP推理服务

```bash
./server -m models/llama-3.1-8b.Q4_K_M.gguf --host 0.0.0.0 --port 8080
```

### 示例 3: GPU卸载35层，8K上下文推理

```bash
./main -m model.gguf -ngl 35 -c 8192
```

## 使用场景

- **CPU/低显存推理**：无 GPU 或仅集显环境运行量化 LLM。
- **端侧/嵌入式部署**：编译为单一二进制，便于分发到边缘设备。
- **量化实验**：对比不同 GGUF 量化等级的质量与速度。

## 生产环境最佳实践

- 编译时按硬件启用加速：`-DGGML_CUDA=ON`（NVIDIA）、`-DGGML_METAL=ON`（Apple）、`-DGGML_BLAS=ON`（CPU）。
- 用 `llama-server` 提供 OpenAI 兼容 API，`-ngl` 控制 offload 到 GPU 的层数。
- `-c` 设置上下文长度，`-t` 设置 CPU 线程数（一般等于物理核数）。
- 量化选型：q4_K_M 兼顾质量与体积，q8_0 接近原始精度，q2/q3 仅用于极端受限场景。
- 批量/并发用 `--parallel` 与 `--cont-batching`。

## 故障排除

| 现象 | 可能原因 | 处理 |
|------|----------|------|
| GPU 未被利用 | 未编译 CUDA/未设 -ngl | 按 `-DGGML_CUDA=ON` 重新编译并加 `-ngl 999` |
| 输出乱码 | chat 模板不匹配 | 指定正确 `--chat-template` 或使用官方 GGUF |
| 加载失败 | GGUF 版本过旧 | 用最新 `convert_hf_to_gguf.py` 重新转换 |
| 速度慢 | 线程/量化不当 | 调 `-t` 至物理核数，改用 K-quant |

## 关联与依赖

- **上游**：由 HuggingFace 权重经 `gguf-convert`（convert_hf_to_gguf.py）转 GGUF。
- **封装**：[[ollama]] 在其之上提供更易用的模型管理层。
- **生产替代**：高并发 GPU 场景选 [[vllm]]。

## 安全与风险注意事项

- `llama-server` 默认无鉴权，对外暴露需加反向代理认证。
- GGUF 文件来自不可信来源存在供应链风险，建议校验发布者与哈希。

## 关联命令

- [[ollama]]
- [[gguf-convert]]

## 风险提示

> ⚠️ **LOW**: 本地推理无网络风险

## 参考链接

- [https://github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
