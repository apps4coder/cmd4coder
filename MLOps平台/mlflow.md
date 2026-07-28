---
{
  "cmd_name": "mlflow",
  "cmd_category": "AI基础设施/MLOps平台",
  "cmd_dimension": "MLOps平台",
  "cmd_install": "pip install mlflow",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kfp"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/mlops.yaml"
}
---

# mlflow

> MLflow 命令行客户端，用于模型全生命周期管理

## 安装

```bash
pip install mlflow
```

## 用法

```
mlflow [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行一个MLflow项目 |
| `ui` | 启动MLflow跟踪UI |
| `models` | 管理模型 (serve, predict, build-docker) |
| `artifacts` | 下载或上传产物 |

## 示例

### 示例 1: 启动UI，使用SQLite作为后端存储

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

### 示例 2: 运行当前项目的'train'入口点，并传递参数

```bash
mlflow run . -e train --P alpha=0.5
```

### 示例 3: 将指定运行产出的模型部署为一个本地服务

```bash
mlflow models serve -m runs:/<run_id>/model -p 1234
```

## 使用场景

- **实验跟踪**：记录参数、指标、产物，对比多次训练。
- **模型注册与版本管理**：用 Model Registry 管理阶段（Staging/Production）。
- **模型部署**：`mlflow models serve` 将模型包装为 REST 服务或 Docker 镜像。

## 生产环境最佳实践

- 生产用独立 Tracking Server + 后端数据库（Postgres/MySQL），产物存对象存储（S3/MinIO）。
- 统一用 `--backend-store-uri` 与 `--default-artifact-root` 配置，避免 SQLite 上生产（无并发）。
- 用 `MLFLOW_TRACKING_URI` 环境变量解耦代码与服务地址。
- 用 autolog（`mlflow.autolog()`）减少手动埋点，保证指标完整。
- 模型升级通过 Registry 阶段转换（transition_model_version_stage），配合 CI 审批。

## 故障排除

| 现象 | 可能原因 | 处理 |
|------|----------|------|
| UI 看不到运行 | tracking uri 不一致 | 确保客户端与 UI 指向同一 `--backend-store-uri` |
| 产物下载失败 | artifact root 不可达 | 校对 S3/MinIO 凭证与 `--default-artifact-root` |
| serve 报依赖缺失 | 环境与训练不一致 | 用 `--env-manager conda/virtualenv` 重建依赖 |
| 并发写报错 | SQLite 锁 | 换 Postgres/MySQL 作为后端存储 |

## 关联与依赖

- **同类/互补**：[[kfp]]（Kubeflow Pipelines）、[[dagster]]/[[prefect]]（编排）、[[kedro]]（工程化）。
- **存储依赖**：后端数据库（元数据）+ 对象存储（产物）。
- **集成**：transformers/PyTorch/sklearn 均有 autolog 支持。

## 安全与风险注意事项

- Tracking Server 默认无鉴权，生产需前置反向代理认证，避免实验数据与模型被任意访问。
- `mlflow run`/`models serve` 会创建环境并执行代码，勿运行不可信项目。

## 关联命令

- [[kfp]]

## 风险提示

> ⚠️ **MEDIUM**: 会修改本地环境或依赖

## 参考链接

- [https://mlflow.org/docs/latest/cli.html](https://mlflow.org/docs/latest/cli.html)

## 所属维度

[[MLOps平台-MOC|AI基础设施/MLOps平台]]
