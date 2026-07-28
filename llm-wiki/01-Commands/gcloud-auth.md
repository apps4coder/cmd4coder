---
{
  "cmd_name": "gcloud auth",
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
    "gcloud",
    "gcloud config"
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

# gcloud auth

> 管理 GCP 认证和授权

## 安装

```bash
同 gcloud
```

## 用法

```
gcloud auth login
```

```
gcloud auth activate-service-account
```

## 参数

| Flag | Description |
|------|-------------|
| `--brief` | 简洁输出 |
| `--force` | 强制重新认证 |

## 示例

### 示例 1: 浏览器 OAuth 登录

```bash
gcloud auth login
```

### 示例 2: 使用服务账号密钥认证

```bash
gcloud auth activate-service-account --key-file=sa.json
```

### 示例 3: 获取当前访问令牌

```bash
gcloud auth print-access-token
```

### 示例 4: 设置应用默认凭证

```bash
gcloud auth application-default login
```

## 关联命令

- [[gcloud|gcloud]]

## 风险提示

> ⚠️ **HIGH**: 服务账号密钥文件需妥善保管，泄露可导致资源被滥用

## 所属维度

[[GCP CLI-MOC|云平台/GCP CLI]]
