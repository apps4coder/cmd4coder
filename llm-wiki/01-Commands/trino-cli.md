---
{
  "cmd_name": "trino-cli",
  "cmd_category": "大数据/调度与转换",
  "cmd_dimension": "调度与转换",
  "cmd_install": "下载 Trino CLI JAR 或 brew install trino (macOS)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "clickhouse-client",
    "spark-sql"
  ],
  "cmd_tags": [
    "data",
    "distributed",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/bigdata/orchestration.yaml"
}
---

# trino-cli

> Trino (原 PrestoSQL) 分布式 SQL 查询引擎 CLI

## 安装

```bash
下载 Trino CLI JAR 或 brew install trino (macOS)
```

## 用法

```
trino [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--server` | 服务器地址 |
| `--catalog` | 默认 catalog |
| `--schema` | 默认 schema |
| `--execute` | 执行 SQL 后退出 |
| `--output-format` | 输出格式 |

## 示例

### 示例 1: 交互式连接

```bash
trino --server localhost:8080 --catalog hive --schema default
```

### 示例 2: 执行单条查询

```bash
trino --server localhost:8080 --execute "SELECT * FROM events LIMIT 10"
```

### 示例 3: 跨数据源查询 PostgreSQL

```bash
trino --server localhost:8080 --catalog postgres --schema public --execute "SHOW TABLES"
```

## 关联命令

- [[clickhouse-client|clickhouse-client]]
- [[spark-sql|spark-sql]]

## 风险提示

> ⚠️ **MEDIUM**: 可跨数据源执行写操作（取决于 connector 配置）

## 最佳实践

[[bp-trino-cli|trino-cli 生产环境最佳实践]]

## 所属维度

[[调度与转换-MOC|大数据/调度与转换]]
