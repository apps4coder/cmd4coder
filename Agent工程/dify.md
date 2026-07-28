---
{
  "cmd_name": "dify",
  "cmd_category": "AI基础设施/Agent工程",
  "cmd_dimension": "Agent工程",
  "cmd_install": "docker pull langgenius/dify-api",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "flowise",
    "langchain"
  ],
  "cmd_tags": [
    "agent",
    "application",
    "rag",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/agent-engineering.yaml"
}
---

# dify

> Dify开源LLM应用开发平台，可视化编排Agent、RAG、工作流，支持自托管

## 安装

```bash
docker pull langgenius/dify-api
```

## 用法

```
docker compose up (自托管)
```

## 参数

| Flag | Description |
|------|-------------|
| `--env-file` | 环境变量文件 |

## 示例

### 示例 1: Docker Compose自托管Dify

```bash
git clone https://github.com/langgenius/dify.git && cd dify/docker && docker compose up -d
```

### 示例 2: 含中间件完整部署

```bash
docker compose -f docker-compose.yaml -f docker-compose.middleware.yaml up -d
```

## 使用场景

- **低代码 LLM 应用**：可视化编排 Agent、RAG、工作流，快速交付。
- **企业自托管**：数据与知识库保留在内网，满足合规。
- **多模型统一接入**：在一个平台管理多个提供商与应用。

## 生产环境最佳实践

- 修改 `.env` 中的 `SECRET_KEY`、数据库口令与 `CONSOLE_API_URL`，勿用默认值上生产。
- 向量库（默认 Weaviate）可切换为 Qdrant/pgvector 并独立部署以便扩容。
- 前置反向代理（Nginx）启用 HTTPS，限制控制台映射端口对外暴露。
- 定期备份 Postgres 与向量库，知识库重建成本高。
- 用独立对象存储（S3/MinIO）保存上传文件，避免容器本地盘膨胀。

## 故障排除

| 现象 | 可能原因 | 处理 |
|------|----------|------|
| 登录后接口 404/跨域 | CONSOLE/API URL 配错 | 校对 `.env` 中各 URL 与实际访问域名一致 |
| 知识库检索为空 | Embedding/向量库未就绪 | 检查 embedding 模型配置与向量库容器状态 |
| 容器反复重启 | 资源不足/依赖未就绪 | 确认内存充足，按依赖顺序启动中间件 |
| 文件上传失败 | 存储后端未配 | 配置 S3/MinIO 或校对本地卷权限 |

## 关联与依赖

- **运行依赖**：Docker/Docker Compose、Postgres、Redis、向量库。
- **替代方案**：[[flowise]]（轻量可视化）、[[langchain]]（代码级灵活度更高）。
- **模型后端**：可接 [[ollama]] 本地模型或商用 API（经 [[openrouter]] 网关）。

## 安全与风险注意事项

- 自托管默认配置不适合直接上生产，必须更换密钥、启用认证与 HTTPS。
- 知识库可能包含敏感企业数据，需控制成员权限与外部模型调用的数据外流。

## 关联命令

- [[flowise]]
- [[langchain]]

## 风险提示

> ⚠️ **MEDIUM**: 自托管需配置安全认证

## 参考链接

- [https://dify.ai/](https://dify.ai/)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
