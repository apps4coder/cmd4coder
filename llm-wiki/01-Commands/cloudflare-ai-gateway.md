---
{
  "cmd_name": "cloudflare-ai-gateway",
  "cmd_category": "AI基础设施/AI网关",
  "cmd_dimension": "AI网关",
  "cmd_install": "通过Cloudflare Dashboard或wrangler配置",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "helicone",
    "litellm"
  ],
  "cmd_tags": [
    "edge",
    "gateway",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/ai-gateway.yaml"
}
---

# cloudflare-ai-gateway

> Cloudflare AI Gateway 边缘LLM网关，提供缓存、限速、重试与分析，无需改代码仅改端点

## 安装

```bash
通过Cloudflare Dashboard或wrangler配置
```

## 用法

```
将provider端点改为 https://gateway.ai.cloudflare.com/v1/<account>/<gateway>/<provider>
```

## 参数

| Flag | Description |
|------|-------------|
| `caching` | 开启响应缓存降低重复调用成本 |
| `rate limiting` | 按频率限制保护后端 |
| `fallback` | provider不可用时自动回退 |

## 示例

### 示例 1: 通过网关代理OpenAI请求

```bash
curl https://gateway.ai.cloudflare.com/v1/<acct>/<gw>/openai/chat/completions
```

### 示例 2: 为请求设置缓存TTL降低重复调用成本

```bash
curl https://gateway.ai.cloudflare.com/v1/<acct>/<gw>/openai/chat/completions -H 'cf-aig-cache-ttl: 3600'
```

## 关联命令

- [[helicone|helicone]]
- [[litellm|litellm]]

## 风险提示

> ⚠️ **LOW**: 缓存命中时不调用后端，需注意敏感/个性化响应不宜缓存

## 参考链接

- [https://developers.cloudflare.com/ai-gateway/](https://developers.cloudflare.com/ai-gateway/)

## 所属维度

[[AI网关-MOC|AI基础设施/AI网关]]
