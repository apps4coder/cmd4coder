---
{
  "cmd_name": "az storage",
  "cmd_category": "云平台/Azure CLI",
  "cmd_dimension": "Azure CLI",
  "cmd_install": "同 az",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "az",
    "aws s3"
  ],
  "cmd_tags": [
    "rag",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/azure.yaml"
}
---

# az storage

> 管理 Azure Storage 账户、Blob、文件共享

## 安装

```bash
同 az
```

## 用法

```
az storage [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--account-name` | 存储账户名 |
| `--account-key` | 存储账户密钥 |
| `--connection-string` | 连接字符串 |
| `--container-name` | Blob 容器名 |

## 示例

### 示例 1: 列出存储账户

```bash
az storage account list --output table
```

### 示例 2: 创建 Blob 容器

```bash
az storage container create --name my-container --account-name mystorage
```

### 示例 3: 上传文件到 Blob

```bash
az storage blob upload --account-name mystorage --container-name my-container --file ./data.csv --name data.csv
```

### 示例 4: 列出容器内 Blob

```bash
az storage blob list --account-name mystorage --container-name my-container --output table
```

## 关联命令

- [[az|az]]
- [[aws-s3|aws s3]]

## 风险提示

> ⚠️ **MEDIUM**: 密钥泄露可导致数据被访问，delete 操作不可逆

## 最佳实践

[[bp-az-storage|az storage 生产环境最佳实践]]

## 所属维度

[[Azure CLI-MOC|云平台/Azure CLI]]
