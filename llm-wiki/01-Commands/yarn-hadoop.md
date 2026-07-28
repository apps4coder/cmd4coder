---
{
  "cmd_name": "yarn (Hadoop)",
  "cmd_category": "大数据/流处理",
  "cmd_dimension": "流处理",
  "cmd_install": "随 Hadoop 发行版安装",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "hdfs",
    "spark-submit"
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

# yarn (Hadoop)

> Hadoop YARN 资源管理器 CLI

## 安装

```bash
随 Hadoop 发行版安装
```

## 用法

```
yarn [命令] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `application` | 应用管理 |
| `node` | 节点管理 |
| `queue` | 队列管理 |
| `logs` | 查看日志 |

## 示例

### 示例 1: 列出运行中的应用

```bash
yarn application -list
```

### 示例 2: 终止指定应用

```bash
yarn application -kill <app-id>
```

### 示例 3: 查看应用日志

```bash
yarn logs -applicationId <app-id>
```

### 示例 4: 列出集群节点

```bash
yarn node -list
```

### 示例 5: 查看队列状态

```bash
yarn queue -status default
```

## 关联命令

- [[hdfs|hdfs]]
- [[spark-submit|spark-submit]]

## 风险提示

> ⚠️ **HIGH**: -kill 终止运行中的计算任务

## 所属维度

[[流处理-MOC|大数据/流处理]]
