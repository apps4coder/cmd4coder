---
{
  "cmd_name": "nemo-guardrails",
  "cmd_category": "AI基础设施/AI安全",
  "cmd_dimension": "AI安全",
  "cmd_install": "pip install nemoguardrails",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "llm-guard",
    "rebuff"
  ],
  "cmd_tags": [
    "safety",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/ai-safety.yaml"
}
---

# nemo-guardrails

> NVIDIA NeMo Guardrails 可编程护栏框架，用Colang定义对话边界、事实性与安全策略

## 安装

```bash
pip install nemoguardrails
```

## 用法

```
nemoguardrails [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `chat` | 启动带护栏的交互式对话 |
| `server` | 启动护栏API服务端 |
| `--config` | 指定护栏配置目录 (rails + Colang) |

## 示例

### 示例 1: 基于配置目录启动护栏服务

```bash
nemoguardrails server --config ./config
```

### 示例 2: 本地测试护栏拦截效果

```bash
nemoguardrails chat --config ./config
```

## 关联命令

- [[llm-guard|llm-guard]]
- [[rebuff|rebuff]]

## 风险提示

> ⚠️ **MEDIUM**: Colang规则误配可能过度拦截正常请求或放行恶意输入

## 参考链接

- [https://github.com/NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)

## 最佳实践

[[bp-nemo-guardrails|nemo-guardrails 生产环境最佳实践]]

## 所属维度

[[AI安全-MOC|AI基础设施/AI安全]]
