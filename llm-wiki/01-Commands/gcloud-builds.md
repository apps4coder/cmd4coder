---
{
  "cmd_name": "gcloud builds",
  "cmd_category": "云平台/GCP CLI",
  "cmd_dimension": "GCP CLI",
  "cmd_install": "同 gcloud",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "gcloud run",
    "gcloud container"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/gcloud.yaml"
}
---

# gcloud builds

> 管理 Cloud Build CI/CD 构建

## 安装

```bash
同 gcloud
```

## 用法

```
gcloud builds submit [参数]
```

```
gcloud builds log [命令]
```

## 参数

| Flag | Description |
|------|-------------|
| `--tag` | 构建镜像标签 |
| `--config` | 指定 cloudbuild.yaml 配置文件 |
| `--timeout` | 构建超时时间 |

## 示例

### 示例 1: 提交本地代码构建容器镜像

```bash
gcloud builds submit --tag gcr.io/project/app:v1
```

### 示例 2: 使用配置文件执行构建

```bash
gcloud builds submit --config cloudbuild.yaml
```

### 示例 3: 列出构建历史

```bash
gcloud builds log list
```

### 示例 4: 查看最近 5 次构建日志

```bash
gcloud builds log read --limit=5
```

## 关联命令

- [[gcloud-run|gcloud run]]
- [[gcloud-container|gcloud container]]

## 风险提示

> ⚠️ **LOW**: 构建操作风险较低，但会产生 Cloud Build 费用

## 最佳实践

[[bp-gcloud-builds|gcloud builds 生产环境最佳实践]]

## 所属维度

[[GCP CLI-MOC|云平台/GCP CLI]]
