---
{
  "cmd_name": "gcloud iam",
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
    "gcloud auth",
    "gcloud projects"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/gcloud.yaml"
}
---

# gcloud iam

> 管理 IAM 身份和访问控制策略

## 安装

```bash
同 gcloud
```

## 用法

```
gcloud iam [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--member` | 指定成员 (user:/serviceAccount:/group:) |
| `--role` | 指定角色 |

## 示例

### 示例 1: 列出服务账号

```bash
gcloud iam service-accounts list
```

### 示例 2: 查看项目 IAM 策略

```bash
gcloud projects get-iam-policy my-project
```

### 示例 3: 授予用户 editor 角色

```bash
gcloud projects add-iam-policy-binding my-project --member=user:dev@example.com --role=roles/editor
```

### 示例 4: 创建服务账号密钥

```bash
gcloud iam service-accounts keys create key.json --iam-account=sa@project.iam.gserviceaccount.com
```

## 关联命令

- [[gcloud-auth|gcloud auth]]

## 风险提示

> ⚠️ **HIGH**: IAM 策略变更影响访问权限，密钥文件需妥善保管

## 最佳实践

[[bp-gcloud-iam|gcloud iam 生产环境最佳实践]]

## 所属维度

[[GCP CLI-MOC|云平台/GCP CLI]]
