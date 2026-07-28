---
{
  "cmd_name": "qdrant",
  "cmd_category": "AI基础设施/向量数据库",
  "cmd_dimension": "向量数据库",
  "cmd_install": "docker pull qdrant/qdrant",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "milvus-cli",
    "weaviate-cli"
  ],
  "cmd_tags": [
    "deployment",
    "data",
    "vector-db",
    "distributed",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/vector-db.yaml"
}
---

# qdrant

> Qdrant高性能开源向量数据库，支持过滤搜索、分布式部署、Rust实现

## 安装

```bash
docker pull qdrant/qdrant
```

## 用法

```
docker run [OPTIONS] qdrant/qdrant
```

```
python app.py (使用qdrant-client)
```

## 参数

| Flag | Description |
|------|-------------|
| `--name` | 容器名称 |
| `-p` | 端口映射 |
| `-v` | 数据卷挂载 |

## 示例

### 示例 1: Docker启动Qdrant

```bash
docker run -p 6333:6333 -v $(pwd)/qdrant_storage:/qdrant/storage qdrant/qdrant
```

### 示例 2: Python客户端连接

```bash
python -c "from qdrant_client import QdrantClient; client = QdrantClient('localhost', port=6333)"
```

## 使用场景

- **RAG 向量检索**：存储 embedding 并做高性能近似最近邻（ANN）检索。
- **推荐/去重/语义搜索**：带 payload 过滤的混合检索。
- **边缘/嵌入式**：Rust 实现，资源占用低，可嵌入或容器化部署。

## 生产环境最佳实践

- 为 payload 中用于过滤的字段建立 payload index，避免全量扫描。
- 根据召回/延迟需求调 HNSW 参数：`m`、`ef_construct`（建索）与 `hnsw_ef`（查询）。
- 大规模向量启用量化（scalar/product quantization）降内存，配合 `on_disk` 存储。
- 生产启用 API Key 与 TLS，写入用批量 `upsert` 并设合理 `wait`。
- 多副本/分片（collection 的 `shard_number`/`replication_factor`）保障可用性。

## 故障排除

| 现象 | 可能原因 | 处理 |
|------|----------|------|
| 召回率偏低 | hnsw_ef 过小 | 提高查询 `hnsw_ef`，必要时重建索引提高 `ef_construct` |
| 内存占用高 | 未量化/全内存 | 启用 quantization 与 `on_disk` 向量存储 |
| 过滤查询慢 | 缺 payload index | 为过滤字段创建 payload index |
| 写入后查不到 | 未等待索引 | upsert 时设 `wait=true` 或稍后查询 |

## 关联与依赖

- **同类向量库**：[[milvus-cli]]（大规模分布式）、[[weaviate-cli]]、[[pinecone]]（托管）、[[pgvector]]（Postgres 内）。
- **上游**：由 [[sentence-transformers]]/[[fastembed]] 生成 embedding 写入。
- **下游**：为 [[langchain]]/[[dify]] 的 RAG 检索器提供向量存储。

## 安全与风险注意事项

- 默认无鉴权，对外暴露必须启用 API Key 与 TLS，否则向量与 payload 可被任意读取。
- payload 可能存储原文片段等敏感信息，需控制访问与备份加密。

## 关联命令

- [[milvus-cli]]
- [[weaviate-cli]]

## 风险提示

> ⚠️ **LOW**: Docker部署安全可控

## 参考链接

- [https://qdrant.tech/](https://qdrant.tech/)

## 所属维度

[[向量数据库-MOC|AI基础设施/向量数据库]]
