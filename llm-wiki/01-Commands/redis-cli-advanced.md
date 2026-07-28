---
{
  "cmd_name": "redis-cli (advanced)",
  "cmd_category": "数据库工具/运维操作",
  "cmd_dimension": "运维操作",
  "cmd_install": "随 Redis 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "redis-server",
    "redis-sentinel"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/database/operations.yaml"
}
---

# redis-cli (advanced)

> Redis 高级运维操作（集群、持久化、内存分析）

## 安装

```bash
随 Redis 安装
```

## 用法

```
redis-cli [选项] [命令]
```

## 参数

| Flag | Description |
|------|-------------|
| `--bigkeys` | 扫描大 key |
| `--memkeys` | 按内存排序 key |
| `--cluster` | 集群管理 |
| `--rdb` | 导出 RDB 文件 |
| `--pipe` | 批量导入 |

## 示例

### 示例 1: 扫描并报告大 key

```bash
redis-cli --bigkeys
```

### 示例 2: 检查集群健康状态

```bash
redis-cli --cluster check 127.0.0.1:7000
```

### 示例 3: 重新分片

```bash
redis-cli --cluster reshard 127.0.0.1:7000
```

### 示例 4: 查看 key 内存占用

```bash
redis-cli MEMORY USAGE mykey
```

### 示例 5: 查看内存使用详情

```bash
redis-cli INFO memory
```

## 关联命令

- [[redis-server|redis-server]]
- [[redis-sentinel|redis-sentinel]]

## 风险提示

> ⚠️ **HIGH**: reshard 影响集群数据分布，FLUSHALL 清空所有数据

## 所属维度

[[运维操作-MOC|数据库工具/运维操作]]
