---
{
  "cmd_name": "kedro",
  "cmd_category": "AI基础设施/MLOps平台",
  "cmd_dimension": "MLOps平台",
  "cmd_install": "pip install kedro",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "zenml",
    "mlflow"
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

# kedro

> Kedro (麦肯锡QuantumBlack开源) 数据科学工程化框架，Data Catalog+Pipeline约定驱动项目结构

## 安装

```bash
pip install kedro
```

## 用法

```
kedro [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `new` | 从模板创建新项目 |
| `run` | 运行Pipeline (--pipeline, --nodes, --tags过滤) |
| `viz` | 启动可视化Web UI (需kedro-viz) |
| `catalog` | 管理Data Catalog数据集 |

## 示例

### 示例 1: 用官方starter创建示例项目

```bash
kedro new --starter=spaceflights-pandas
```

### 示例 2: 以prod环境配置运行training管道

```bash
kedro run --pipeline=training --env=prod
```

### 示例 3: 打开管道血缘可视化界面

```bash
kedro viz run
```

## 关联命令

- [[zenml|zenml]]
- [[mlflow|mlflow]]

## 风险提示

> ⚠️ **LOW**: --env 切换环境配置，误用prod环境可能覆盖生产数据集

## 参考链接

- [https://docs.kedro.org/en/stable/development/commands_reference.html](https://docs.kedro.org/en/stable/development/commands_reference.html)

## 最佳实践

[[bp-kedro|kedro 生产环境最佳实践]]

## 所属维度

[[MLOps平台-MOC|AI基础设施/MLOps平台]]
