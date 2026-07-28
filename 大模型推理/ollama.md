---
{
  "cmd_name": "ollama",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "curl -fsSL https://ollama.com/install.sh | sh",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "llama.cpp",
    "vllm"
  ],
  "cmd_tags": [
    "inference",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-inference.yaml"
}
---

# ollama

> Ollama本地大模型运行管理工具，一键下载和运行各类开源模型

## 安装

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## 用法

```
ollama [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行模型 |
| `pull` | 下载模型 |
| `list` | 列出本地模型 |
| `serve` | 启动API服务 |
| `create` | 从Modelfile创建模型 |

## 示例

### 示例 1: 下载并运行LLaMA-3.1模型

```bash
ollama run llama3.1
```

### 示例 2: 运行Qwen2-72B模型

```bash
ollama run qwen2:72b
```

### 示例 3: 启动Ollama API服务(默认端口11434)

```bash
ollama serve
```

### 示例 4: 使用Modelfile创建自定义模型

```bash
ollama create my-model -f Modelfile
```

## 使用场景

- **本地开发与原型**：一条命令拉起模型，零配置对接 OpenAI 兼容 API（`localhost:11434`）。
- **离线/隐私场景**：数据不出内网的本地推理，满足合规要求。
- **边缘/个人设备**：Mac、消费级 GPU 上运行量化模型。

## 生产环境最佳实践

- `OLLAMA_HOST=0.0.0.0` 对外服务，但务必前置反向代理做鉴权（Ollama 本身无认证）。
- 用 `OLLAMA_MODELS` 指定模型存储路径，避免占满系统盘。
- `OLLAMA_KEEP_ALIVE` 控制模型驻留显存时间，频繁调用设长、省显存设短或 `0`。
- 用 `Modelfile` + `ollama create` 固化系统提示与参数，保证可复现部署。
- `OLLAMA_NUM_PARALLEL`与 `OLLAMA_MAX_LOADED_MODELS` 控制并发与模型缓存。

## 故障排除

| 现象 | 可能原因 | 处理 |
|------|----------|------|
| 推理只跑 CPU | 未识别 GPU/驱动缺失 | 检查 `nvidia-smi`、确认 CUDA 驱动与 Ollama 版本兼容 |
| 模型响应极慢 | 显存不足回退到内存 | 换更小量化变体（q4_K_M）或增大显存 |
| 端口占用 | 已有实例运行 | `OLLAMA_HOST` 换端口或停止旧进程 |
| 模型反复重新加载 | KEEP_ALIVE 过短 | 调大 `OLLAMA_KEEP_ALIVE`（如 `24h`） |

## 关联与依赖

- **底层**：基于 [[llamacpp]] 的 GGUF 推理，模型可由 `gguf-convert` 生成。
- **进阶替代**：高并发生产场景建议改用 [[vllm]]（更高吞吐、张量并行）。
- **生态**：可作为 [[dify]]、LangChain 等应用的本地模型后端。

## 安全与风险注意事项

- 默认监听无鉴权，`0.0.0.0` 暴露到公网等于开放推理算力，必须加认证与防火墙。
- 拉取的第三方模型可能包含未经审计内容，生产前需评估来源与许可证。

## 关联命令

- [[llamacpp]]
- [[vllm]]

## 风险提示

> ⚠️ **LOW**: 本地运行，风险可控

## 参考链接

- [https://ollama.com/](https://ollama.com/)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
