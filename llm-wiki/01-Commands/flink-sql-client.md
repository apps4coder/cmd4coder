---
{
  "cmd_name": "flink sql-client",
  "cmd_category": "大数据/流处理",
  "cmd_dimension": "流处理",
  "cmd_install": "同 flink",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "flink"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/bigdata/streaming.yaml"
}
---

# flink sql-client

> Flink SQL 交互式客户端

## 安装

```bash
同 flink
```

## 用法

```
sql-client.sh [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `embedded` | 嵌入式模式 |
| `-f` | 执行 SQL 文件 |
| `-i` | 初始化 SQL 文件 |

## 示例

### 示例 1: 启动交互式 SQL 客户端

```bash
sql-client.sh embedded
```

### 示例 2: 执行 SQL 文件

```bash
sql-client.sh -f queries.sql
```

### 示例 3: 加载初始化配置后启动

```bash
sql-client.sh -i init.sql embedded
```

## 关联命令

- [[flink|flink]]

## 风险提示

> ⚠️ **MEDIUM**: SQL 操作可能创建/修改/删除表和作业

## 所属维度

[[流处理-MOC|大数据/流处理]]
