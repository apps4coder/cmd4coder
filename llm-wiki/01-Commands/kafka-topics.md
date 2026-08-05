---
{
  "cmd_name": "kafka-topics",
  "cmd_category": "大数据/流处理",
  "cmd_dimension": "流处理",
  "cmd_install": "随 Apache Kafka 发行版安装或 brew install kafka (macOS)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kafka-console-producer",
    "kafka-consumer-groups"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/bigdata/streaming.yaml"
}
---

# kafka-topics

> Kafka Topic 管理工具（创建、删除、查看、修改分区）

## 安装

```bash
随 Apache Kafka 发行版安装或 brew install kafka (macOS)
```

## 用法

```
kafka-topics.sh [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--bootstrap-server` | Kafka 集群地址 |
| `--create` | 创建 Topic |
| `--delete` | 删除 Topic |
| `--describe` | 查看 Topic 详情 |
| `--partitions` | 分区数 |
| `--replication-factor` | 副本因子 |
| `--alter` | 修改 Topic 配置 |

## 示例

### 示例 1: 创建 6 分区 3 副本的 Topic

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --create --topic orders --partitions 6 --replication-factor 3
```

### 示例 2: 列出所有 Topic

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --list
```

### 示例 3: 查看 Topic 分区和副本分布

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic orders
```

### 示例 4: 扩容分区到 12（不可缩容）

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --alter --topic orders --partitions 12
```

## 关联命令

- [[kafka-console-producer|kafka-console-producer]]
- [[kafka-consumer-groups|kafka-consumer-groups]]

## 风险提示

> ⚠️ **HIGH**: --delete 删除 Topic 数据不可逆，--alter 分区不可缩容

## 最佳实践

[[bp-kafka-topics|kafka-topics 生产环境最佳实践]]

## 所属维度

[[流处理-MOC|大数据/流处理]]
