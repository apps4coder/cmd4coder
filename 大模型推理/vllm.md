---
{
  "cmd_name": "vllm",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "pip install vllm",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "sglang",
    "lmdeploy"
  ],
  "cmd_tags": [
    "inference",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-inference.yaml"
}
---

# vllm

> vLLM高性能大模型推理引擎，采用PagedAttention实现最高24倍吞吐提升

## 安装

```bash
pip install vllm
```

## 用法

```
vllm serve [OPTIONS]
```

```
python -m vllm.entrypoints.openai.api_server [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--model` | 模型路径或HuggingFace模型ID |
| `--tensor-parallel-size` | 张量并行GPU数量 |
| `--max-model-len` | 最大序列长度 |
| `--gpu-memory-utilization` | GPU内存利用率上限(0.0-1.0) |
| `--quantization` | 量化方式 (awq, gptq, fp8) |

## 示例

### 示例 1: 2卡张量并行部署LLaMA-3.1-8B

```bash
vllm serve meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 2
```

### 示例 2: 8卡部署Qwen2-72B，支持32K上下文

```bash
vllm serve Qwen/Qwen2-72B --tensor-parallel-size 8 --max-model-len 32768
```

### 示例 3: AWQ量化部署，节省显存

```bash
vllm serve TheBloke/Llama-2-70B-AWQ --quantization awq --gpu-memory-utilization 0.9
```

## 使用场景

- **在线高并发推理**：对外提供 OpenAI 兼容 API，支撑聊天/RAG 应用后端。
- **多租户 LLM 网关后端**：配合 openrouter/portkey 做统一入口与计费。
- **离线批量推理**：用 `LLM.generate()` 做大规模数据标注与评测集打分。

## 生产环境最佳实践

- `--gpu-memory-utilization` 建议 0.90~0.95，为激活值与碎片预留余量，过高易触发 OOM。
- 显式设置 `--max-model-len` 限制上下文长度，KV Cache 显存随其线性增长。
- 单机多卡用 `--tensor-parallel-size=GPU数`；跨机再叠加 `--pipeline-parallel-size` + Ray 集群。
- 开启 `--enable-prefix-caching` 复用相同系统提示前缀，显著降低重复计算。
- 用 `--served-model-name` 暴露稳定别名，解耦客户端与底层权重路径。
- 显存紧张时启用 `--quantization awq/fp8` 与 `--kv-cache-dtype fp8`。

## 故障排除

| 现象 | 可能原因 | 处理 |
|------|----------|------|
| CUDA out of memory | KV Cache/权重超显存 | 调低 `--gpu-memory-utilization`、`--max-model-len`、`--max-num-seqs` |
| 吞吐远低于预期 | 并发批太小 | 增大 `--max-num-seqs`，确认未被 `--max-model-len` 卡住 |
| 多卡启动卡死 | NCCL/端口/P2P 问题 | 检查 `--master_port` 冲突、设 `NCCL_DEBUG=INFO`、核对 GPU P2P 拓扑 |
| 权重加载缓慢 | 反复走 HF 下载 | 使用本地权重目录并设 `HF_HUB_OFFLINE=1` |

## 关联与依赖

- **运行依赖**：CUDA + PyTorch，需与 GPU 驱动版本匹配。
- **替代方案**：[[tensorrt-llm]]（极致性能，需编译）、[[sglang]]（RadixAttention）、[[lmdeploy]]（TurboMind）。
- **上下游**：上游用 `huggingface-cli` 拉取权重，下游由 [[openrouter]]/[[portkey]] 等网关聚合。

## 安全与风险注意事项

- OpenAI 兼容端点默认**无鉴权**，生产必须加 `--api-key` 或前置网关做认证与限流。
- 高并发下 KV Cache 可能瞬间耗尽显存导致服务雪崩，需配合队列限流与熔断。
- 加载不可信第三方权重存在供应链风险，建议校验来源与哈希。

## 关联命令

- [[sglang]]
- [[lmdeploy]]

## 风险提示

> ⚠️ **MEDIUM**: 高并发推理可能耗尽GPU资源

## 参考链接

- [https://docs.vllm.ai/](https://docs.vllm.ai/)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
