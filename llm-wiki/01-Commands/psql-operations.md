---
{
  "cmd_name": "psql (operations)",
  "cmd_category": "数据库工具/运维操作",
  "cmd_dimension": "运维操作",
  "cmd_install": "随 PostgreSQL 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "pg_dump",
    "pg_basebackup"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/database/operations.yaml"
}
---

# psql (operations)

> PostgreSQL 运维操作（VACUUM、复制、扩展）

## 安装

```bash
随 PostgreSQL 安装
```

## 用法

```
psql [选项] -c "[SQL]"
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | 执行命令 |
| `-x` | 扩展显示模式 |
| `--no-psqlrc` | 不加载配置 |

## 示例

### 示例 1: 清理并更新统计信息

```bash
psql -c "VACUUM ANALYZE users;"
```

### 示例 2: 查看活跃查询

```bash
psql -c "SELECT * FROM pg_stat_activity WHERE state = 'active';"
```

### 示例 3: 查看复制状态

```bash
psql -c "SELECT * FROM pg_stat_replication;"
```

### 示例 4: 安装扩展

```bash
psql -c "CREATE EXTENSION IF NOT EXISTS pg_trgm;"
```

### 示例 5: 查看数据库大小

```bash
psql -c "SELECT pg_size_pretty(pg_database_size('mydb'));"
```

## 关联命令

- [[pg_dump|pg_dump]]
- [[pg_basebackup|pg_basebackup]]

## 风险提示

> ⚠️ **MEDIUM**: VACUUM FULL 锁表，pg_terminate_backend 终止连接

## 所属维度

[[运维操作-MOC|数据库工具/运维操作]]
