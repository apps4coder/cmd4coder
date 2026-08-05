---
{
  "cmd_name": "gcloud run",
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
    "gcloud container",
    "gcloud builds"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/gcloud.yaml"
}
---

# gcloud run

> 管理 Cloud Run 无服务器容器服务

## 安装

```bash
同 gcloud
```

## 用法

```
gcloud run deploy [服务名] [参数]
```

```
gcloud run services [命令]
```

## 参数

| Flag | Description |
|------|-------------|
| `--image` | 容器镜像地址 |
| `--platform` | 平台 (managed/gke) |
| `--allow-unauthenticated` | 允许未认证访问 |
| `--memory` | 内存限制 (256Mi/512Mi/1Gi) |

## 示例

### 示例 1: 部署容器到 Cloud Run

```bash
gcloud run deploy my-service --image gcr.io/project/app:v1
```

### 示例 2: 列出所有 Cloud Run 服务

```bash
gcloud run services list
```

### 示例 3: 查看服务详情

```bash
gcloud run services describe my-service
```

### 示例 4: 删除 Cloud Run 服务

```bash
gcloud run services delete my-service
```

## 关联命令

- [[gcloud-container|gcloud container]]
- [[gcloud-builds|gcloud builds]]

## 风险提示

> ⚠️ **MEDIUM**: --allow-unauthenticated 会公开服务，注意安全性

## 最佳实践

[[bp-gcloud-run|gcloud run 生产环境最佳实践]]

## 所属维度

[[GCP CLI-MOC|云平台/GCP CLI]]
