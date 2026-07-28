---
{
  "cmd_name": "dagster",
  "cmd_category": "AI基础设施/MLOps平台",
  "cmd_dimension": "MLOps平台",
  "cmd_install": "pip install dagster dagster-webserver",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "airflow",
    "prefect"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/mlops.yaml"
}
---

# dagster

> Dagster 数据编排平台CLI，以软件定义资产(SDA)组织ML管道，内置数据血缘

## 安装

```bash
pip install dagster dagster-webserver
```

## 用法

```
dagster [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `dev` | 启动本地开发环境 (webserver + daemon) |
| `asset materialize` | 物化指定资产 |
| `job launch` | 启动Job运行 |
| `instance info` | 查看实例配置信息 |

## 示例

### 示例 1: 加载pipeline定义并启动本地UI (localhost:3000)

```bash
dagster dev -f pipeline.py
```

### 示例 2: 物化embeddings_table资产及其依赖

```bash
dagster asset materialize -f pipeline.py --select embeddings_table
```

### 示例 3: 按配置文件启动训练Job

```bash
dagster job launch -j train_job -c run_config.yaml
```

## 关联命令

- [[airflow|airflow]]
- [[prefect|prefect]]

## 风险提示

> ⚠️ **LOW**: dev 模式无认证，生产需部署dagster-webserver并配置RBAC

## 参考链接

- [https://docs.dagster.io/_apidocs/cli](https://docs.dagster.io/_apidocs/cli)

## 所属维度

[[MLOps平台-MOC|AI基础设施/MLOps平台]]
