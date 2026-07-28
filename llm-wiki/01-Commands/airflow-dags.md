---
{
  "cmd_name": "airflow dags",
  "cmd_category": "大数据/调度与转换",
  "cmd_dimension": "调度与转换",
  "cmd_install": "同 airflow",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "airflow",
    "airflow tasks"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/bigdata/orchestration.yaml"
}
---

# airflow dags

> Airflow DAG 管理子命令

## 安装

```bash
同 airflow
```

## 用法

```
airflow dags [命令] [dag_id]
```

## 参数

| Flag | Description |
|------|-------------|
| `list` | 列出 DAG |
| `trigger` | 触发 DAG |
| `pause / unpause` | 暂停/恢复 DAG |
| `state` | 查看 DAG 状态 |
| `backfill` | 回填执行 |

## 示例

### 示例 1: 表格形式列出 DAG

```bash
airflow dags list --output table
```

### 示例 2: 暂停 DAG 调度

```bash
airflow dags pause my_dag
```

### 示例 3: 恢复 DAG 调度

```bash
airflow dags unpause my_dag
```

### 示例 4: 查看指定执行日期的状态

```bash
airflow dags state my_dag 2026-07-19T00:00:00
```

## 关联命令

- [[airflow|airflow]]

## 风险提示

> ⚠️ **MEDIUM**: pause 停止调度，backfill 批量执行

## 所属维度

[[调度与转换-MOC|大数据/调度与转换]]
