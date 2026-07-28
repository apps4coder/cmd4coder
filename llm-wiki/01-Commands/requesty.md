---
{
  "cmd_name": "requesty",
  "cmd_category": "AI基础设施/AI网关",
  "cmd_dimension": "AI网关",
  "cmd_install": "无需安装，修改base_url接入",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "openrouter",
    "litellm"
  ],
  "cmd_tags": [
    "gateway",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/ai-gateway.yaml"
}
---

# requesty

> Requesty 统一LLM路由网关，提供智能回退、成本优化与治理看板，兼容OpenAI SDK

## 安装

```bash
无需安装，修改base_url接入
```

## 用法

```
将 base_url 指向 https://router.requesty.ai/v1
```

## 参数

| Flag | Description |
|------|-------------|
| `base_url` | 将OpenAI客户端base_url指向网关 |
| `routing policy` | 配置模型回退与负载均衡策略 |

## 示例

### 示例 1: 一行环境变量接入网关

```bash
export OPENAI_BASE_URL=https://router.requesty.ai/v1
```

### 示例 2: 通过网关发起带回退策略的请求

```bash
curl https://router.requesty.ai/v1/chat/completions -H 'Authorization: Bearer $REQUESTY_KEY' -d '{"model":"openai/gpt-4o","messages":[]}'
```

## 关联命令

- [[openrouter|openrouter]]
- [[litellm|litellm]]

## 风险提示

> ⚠️ **LOW**: 请求经第三方网关中转，敏感数据需评估合规与日志留存策略

## 参考链接

- [https://requesty.ai/](https://requesty.ai/)

## 所属维度

[[AI网关-MOC|AI基础设施/AI网关]]
