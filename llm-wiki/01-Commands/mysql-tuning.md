---
{
  "cmd_name": "mysql (tuning)",
  "cmd_category": "数据库工具/运维操作",
  "cmd_dimension": "运维操作",
  "cmd_install": "随 MySQL 安装",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mysqldump",
    "pt-query-digest"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/database/operations.yaml"
}
---

# mysql (tuning)

> MySQL 性能调优和状态诊断

## 安装

```bash
随 MySQL 安装
```

## 用法

```
mysql -e "[SQL]" [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `-e` | 执行 SQL |
| `--table` | 表格输出 |

## 示例

### 示例 1: 查看当前连接和查询

```bash
mysql -e "SHOW PROCESSLIST;"
```

### 示例 2: InnoDB 引擎状态（锁、缓冲池）

```bash
mysql -e "SHOW ENGINE INNODB STATUS\G"
```

### 示例 3: 分析查询执行计划

```bash
mysql -e "EXPLAIN ANALYZE SELECT * FROM users WHERE email='x';"
```

### 示例 4: 查看线程状态

```bash
mysql -e "SHOW GLOBAL STATUS LIKE 'Threads%';"
```

### 示例 5: 查看锁等待

```bash
mysql -e "SELECT * FROM information_schema.INNODB_LOCK_WAITS;"
```

## 关联命令

- [[mysqldump|mysqldump]]
- [[pt-query-digest|pt-query-digest]]

## 风险提示

> ⚠️ **LOW**: 查询操作风险低，KILL 终止查询需确认

## 最佳实践

[[bp-mysql-tuning|mysql (tuning) 生产环境最佳实践]]

## 所属维度

[[运维操作-MOC|数据库工具/运维操作]]
