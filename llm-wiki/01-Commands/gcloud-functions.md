---
{
  "cmd_name": "gcloud functions",
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

# gcloud functions

> 管理 Cloud Functions 无服务器函数

## 安装

```bash
同 gcloud
```

## 用法

```
gcloud functions deploy [函数名] [参数]
```

```
gcloud functions [命令]
```

## 参数

| Flag | Description |
|------|-------------|
| `--runtime` | 运行时 (python311/nodejs20/go121) |
| `--trigger-http` | HTTP 触发器 |
| `--trigger-topic` | Pub/Sub 主题触发器 |
| `--memory` | 内存配置 |

## 示例

### 示例 1: 部署 HTTP 触发函数

```bash
gcloud functions deploy hello --runtime python311 --trigger-http
```

### 示例 2: 列出所有函数

```bash
gcloud functions list
```

### 示例 3: 查看函数日志

```bash
gcloud functions logs read hello --limit=20
```

### 示例 4: 删除函数

```bash
gcloud functions delete hello
```

## 关联命令

- [[gcloud-run|gcloud run]]
- [[gcloud-builds|gcloud builds]]

## 风险提示

> ⚠️ **MEDIUM**: 部署会更新生产函数，删除不可逆

## 所属维度

[[GCP CLI-MOC|云平台/GCP CLI]]
