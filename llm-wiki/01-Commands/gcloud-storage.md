---
{
  "cmd_name": "gcloud storage",
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
    "gcloud",
    "aws s3"
  ],
  "cmd_tags": [
    "rag",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/gcloud.yaml"
}
---

# gcloud storage

> 管理 Cloud Storage 存储桶和对象

## 安装

```bash
同 gcloud
```

## 用法

```
gcloud storage [命令] [参数]
```

```
gsutil [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `-r` | 递归操作 |
| `-m` | 并行传输 |

## 示例

### 示例 1: 列出所有存储桶

```bash
gcloud storage buckets list
```

### 示例 2: 上传文件到存储桶

```bash
gcloud storage cp file.txt gs://my-bucket/
```

### 示例 3: 递归同步目录到存储桶

```bash
gcloud storage rsync ./local gs://my-bucket/ -r
```

### 示例 4: 并行递归上传目录

```bash
gsutil -m cp -r ./dist gs://my-bucket/
```

## 关联命令

- [[gcloud|gcloud]]
- [[aws-s3|aws s3]]

## 风险提示

> ⚠️ **MEDIUM**: rsync 和 rm -r 操作可能覆盖或删除远端数据

## 所属维度

[[GCP CLI-MOC|云平台/GCP CLI]]
