---
{
  "cmd_name": "deepspeed",
  "cmd_category": "AI基础设施/大模型训练",
  "cmd_dimension": "大模型训练",
  "cmd_install": "pip install deepspeed",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "accelerate",
    "torchrun"
  ],
  "cmd_tags": [
    "training",
    "distributed",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-training.yaml"
}
---

# deepspeed

> 微软DeepSpeed大规模分布式训练框架，支持ZeRO优化、3D并行、Offload

## 安装

```bash
pip install deepspeed
```

## 用法

```
deepspeed [OPTIONS] SCRIPT.py [ARGS...]
```

## 参数

| Flag | Description |
|------|-------------|
| `--num_gpus` | 使用的GPU数量 |
| `--master_port` | 分布式训练主节点端口 |
| `--include` | 指定使用的GPU，如 'localhost:0,1,2,3' |
| `--exclude` | 排除指定的GPU |

## 示例

### 示例 1: 使用4张GPU和DeepSpeed配置文件启动训练

```bash
deepspeed --num_gpus=4 train.py --deepspeed ds_config.json
```

### 示例 2: 指定使用8张GPU进行训练

```bash
deepspeed --include='localhost:0,1,2,3,4,5,6,7' train.py
```

### 示例 3: 使用ZeRO-3优化策略训练大模型

```bash
deepspeed train.py --deepspeed ds_config_zero3.json
```

## 使用场景

- **大模型全参/指令微调**：单卡放不下时用 ZeRO 分片优化器/梯度/参数。
- **多机多卡训练**：3D 并行（数据/流水/张量）扩展到百卡规模。
- **显存受限微调**：ZeRO-Offload/Infinity 将状态 offload 到 CPU/NVMe。

## 生产环境最佳实践

- 按显存预算选 ZeRO 阶段：Stage 2（分片优化器+梯度）通用，Stage 3（再分片参数）用于超大模型。
- Offload 代价是速度，仅在显存不足时启用 `offload_optimizer`/`offload_param`。
- 启用 `bf16`（Ampere+ 推荐）或 `fp16` 混合精度，配合 gradient checkpointing 降显存。
- 多机用 hostfile + `--num_nodes`，确保节点间 SSH 免密与高速互联（IB/RoCE）。
- 用 `ds_config.json` 集中管理参数，与命令行参数避免重复冲突。

## 故障排除

| 现象 | 可能原因 | 处理 |
|------|----------|------|
| NCCL timeout/挂起 | 网络/拓扑问题 | 设 `NCCL_DEBUG=INFO` 定位，检查 IB、`NCCL_SOCKET_IFNAME` |
| OOM 仍发生 | ZeRO 阶段不足 | 升到 Stage 3，开启 offload 与 gradient checkpointing |
| 启动报端口占用 | master_port 冲突 | 换 `--master_port`，确保各 job 唯一 |
| loss 为 NaN | fp16 溢出 | 改用 bf16 或调整 loss scaling |

## 关联与依赖

- **启动器替代**：[[torchrun]]（原生 DDP）、[[accelerate]]（HuggingFace 封装，可后端接 DeepSpeed）。
- **依赖**：CUDA、NCCL、PyTorch；部分算子需编译（`ds_report` 查看）。
- **上层框架**：LLaMA-Factory、transformers Trainer 均可以 DeepSpeed 为后端。

## 安全与风险注意事项

- 大规模训练长时占用昂贵 GPU 集群，需做好作业配额与抢占策略。
- checkpoint 体积大且含权重，存储与传输需考虑容量、权限与合规。

## 关联命令

- [[accelerate]]
- [[torchrun]]

## 风险提示

> ⚠️ **MEDIUM**: 大规模分布式训练消耗大量GPU资源，需合理配置

## 参考链接

- [https://www.deepspeed.ai/](https://www.deepspeed.ai/)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
