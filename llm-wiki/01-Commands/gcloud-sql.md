---
{
  "cmd_name": "gcloud sql",
  "cmd_category": "云平台/GCP CLI",
  "cmd_dimension": "GCP CLI",
  "cmd_install": "同 gcloud",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "gcloud compute",
    "gcloud storage"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/gcloud.yaml"
}
---

# gcloud sql

> 管理 Cloud SQL 数据库实例

## 安装

```bash
同 gcloud
```

## 用法

```
gcloud sql [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--instance` | 数据库实例名 |
| `--tier` | 机器规格 |
| `--database-version` | 数据库版本 (MYSQL_8_0/POSTGRES_15) |

## 示例

### 示例 1: 列出所有数据库实例

```bash
gcloud sql instances list
```

### 示例 2: 创建 PostgreSQL 实例

```bash
gcloud sql instances create my-db --database-version=POSTGRES_15 --tier=db-f1-micro
```

### 示例 3: 在实例中创建数据库

```bash
gcloud sql databases create mydb --instance=my-db
```

### 示例 4: 连接到数据库实例

```bash
gcloud sql connect my-db --user=postgres
```

## 关联命令

- [[gcloud-compute|gcloud compute]]
- [[gcloud-storage|gcloud storage]]

## 风险提示

> ⚠️ **HIGH**: 数据库实例产生持续费用，删除操作导致数据丢失

## 最佳实践

[[bp-gcloud-sql|gcloud sql 生产环境最佳实践]]

## 所属维度

[[GCP CLI-MOC|云平台/GCP CLI]]
