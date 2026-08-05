---
{
  "cmd_name": "kafka-consumer-groups",
  "cmd_category": "大数据/流处理",
  "cmd_dimension": "流处理",
  "cmd_install": "同 kafka",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kafka-topics",
    "kafka-console-consumer"
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

# kafka-consumer-groups

> Kafka 消费者组管理（查看 lag、重置 offset）

## 安装

```bash
同 kafka
```

## 用法

```
kafka-consumer-groups.sh [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--bootstrap-server` | Kafka 集群地址 |
| `--describe` | 查看消费者组详情 |
| `--group` | 消费者组名 |
| `--reset-offsets` | 重置消费偏移量 |
| `--to-earliest` | 重置到最早 |
| `--to-latest` | 重置到最新 |
| `--execute` | 实际执行（默认为 dry-run） |

## 示例

### 示例 1: 列出所有消费者组

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
```

### 示例 2: 查看消费者组 lag

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-app
```

### 示例 3: 重置 offset 到最早（重新消费）

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --reset-offsets --group my-app --topic orders --to-earliest --execute
```

### 示例 4: 查看消费者组状态

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-app --state
```

## 关联命令

- [[kafka-topics|kafka-topics]]
- [[kafka-console-consumer|kafka-console-consumer]]

## 风险提示

> ⚠️ **HIGH**: --reset-offsets --execute 导致消息重复消费或跳过

## 最佳实践

[[bp-kafka-consumer-groups|kafka-consumer-groups 生产环境最佳实践]]

## 所属维度

[[流处理-MOC|大数据/流处理]]
