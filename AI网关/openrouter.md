---
{
  "cmd_name": "openrouter",
  "cmd_category": "AI基础设施/AI网关",
  "cmd_dimension": "AI网关",
  "cmd_install": "pip install openrouter",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "helicone",
    "portkey"
  ],
  "cmd_tags": [
    "gateway",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/ai-gateway.yaml"
}
---

# openrouter

> OpenRouter统一访问100+开源和商用模型API，标准化接口、自动竞价

## 安装

```bash
pip install openrouter
```

## 用法

```
python app.py (使用openrouter库)
```

```
curl https://openrouter.ai/api/v1/chat/completions
```

## 参数

| Flag | Description |
|------|-------------|
| `HTTP-Referer` | 应用来源标识 |
| `X-Title` | 应用名称 |

## 示例

### 示例 1: 通过OpenRouter调用Claude

```bash
python -c "import openai; client = openai.OpenAI(base_url='https://openrouter.ai/api/v1', api_key='sk-or-xxx'); r = client.chat.completions.create(model='anthropic/claude-3.5-sonnet', messages=[{'role':'user','content':'Hello'}])"
```

### 示例 2: 列出所有可用模型

```bash
curl https://openrouter.ai/api/v1/models | jq '.data[].id'
```

## 使用场景

- **多模型统一接入**：一个 API Key 访问 100+ 开源与商用模型，免逐家开通。
- **成本/可用性优化**：自动路由到性价比或可用的提供商，支持回退。
- **快速选型实验**：在相同接口下对比不同模型效果与价格。

## 生产环境最佳实践

- 直接把 OpenAI 客户端 `base_url` 指向 `https://openrouter.ai/api/v1`，无需改代码逻辑。
- 用 `model` 字段的 `provider/model` 命名（如 `anthropic/claude-3.5-sonnet`）显式指定。
- 配置 `route: fallback` 与 provider 偏好，在限流/宕机时自动切换。
- 设置月度/单请求预算上限，防止异常流量刷爆费用。
- 敏感业务评估数据经第三方中转的合规与日志留存策略。

## 故障排除

| 现象 | 可能原因 | 处理 |
|------|----------|------|
| 401/鉴权失败 | Key 错误/未设 header | 检查 `Authorization: Bearer` 与 `HTTP-Referer`/`X-Title` |
| 模型不可用 | provider 宕机/无额度 | 配置 fallback 或换 `provider/model` |
| 响应字段差异 | 不同 provider 格式差异 | 按 OpenAI 兼容字段解析，容忍额外字段 |
| 费用偏高 | 路由到高价模型 | 锁定模型或设价格上限偏好 |

## 关联与依赖

- **同类网关**：[[portkey]]（可自托管、更多治理）、[[requesty]]、[[cloudflare-ai-gateway]]。
- **可观测互补**：[[helicone]] 做日志/追踪与成本分析。
- **客户端**：兼容 OpenAI SDK，可直接为 [[langchain]]/[[dify]] 提供模型后端。

## 安全与风险注意事项

- 请求经第三方网关中转，敏感数据需评估合规与日志留存，避免传输个人/保密信息。
- API Key 泄露会导致盗刷，应放入密钥管理并设置预算告警。

## 关联命令

- [[helicone]]
- [[portkey]]

## 风险提示

> ⚠️ **LOW**: 第三方API聚合，注意数据安全

## 参考链接

- [https://openrouter.ai/](https://openrouter.ai/)

## 所属维度

[[AI网关-MOC|AI基础设施/AI网关]]
