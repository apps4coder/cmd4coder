---
{
  "cmd_name": "prefect",
  "cmd_category": "AI基础设施/MLOps平台",
  "cmd_dimension": "MLOps平台",
  "cmd_install": "pip install prefect",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "airflow",
    "dagster",
    "metaflow"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/mlops.yaml"
}
---

# prefect

> Prefect 现代化工作流编排CLI，Python原生Flow定义，支持动态DAG与混合执行

## 安装

```bash
pip install prefect
```

## 用法

```
prefect [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `deploy` | 部署Flow到工作池 |
| `worker start` | 启动Worker拉取并执行任务 |
| `server start` | 启动本地Orion服务端 |
| `deployment run` | 触发指定deployment运行 |
| `cloud login` | 登录Prefect Cloud |

## 示例

### 示例 1: 启动本地服务端与UI (默认127.0.0.1:4200)

```bash
prefect server start
```

### 示例 2: 将训练Flow部署到gpu-pool工作池

```bash
prefect deploy ./train.py:train_flow -n nightly-train -p gpu-pool
```

### 示例 3: 启动Worker监听gpu-pool队列

```bash
prefect worker start -p gpu-pool
```

### 示例 4: 手动触发一次部署运行

```bash
prefect deployment run 'train-flow/nightly-train'
```

## 关联命令

- [[airflow|airflow]]
- [[dagster|dagster]]
- [[metaflow|metaflow]]

## 风险提示

> ⚠️ **LOW**: Cloud模式下Flow元数据上传至SaaS，需评估数据合规

## 参考链接

- [https://docs.prefect.io/latest/api-ref/cli/](https://docs.prefect.io/latest/api-ref/cli/)

## 最佳实践

[[bp-prefect|prefect 生产环境最佳实践]]

## 所属维度

[[MLOps平台-MOC|AI基础设施/MLOps平台]]
