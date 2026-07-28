---
{
  "cmd_name": "az keyvault",
  "cmd_category": "云平台/Azure CLI",
  "cmd_dimension": "Azure CLI",
  "cmd_install": "同 az",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "az group",
    "vault"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/azure.yaml"
}
---

# az keyvault

> 管理 Azure Key Vault 密钥、证书和机密

## 安装

```bash
同 az
```

## 用法

```
az keyvault [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--name` | Key Vault 名称 |
| `--resource-group` | 资源组 |
| `--vault-name` | Vault 名称 |

## 示例

### 示例 1: 创建 Key Vault

```bash
az keyvault create --resource-group my-rg --name my-vault --location eastus
```

### 示例 2: 存储机密

```bash
az keyvault secret set --vault-name my-vault --name db-password --value "s3cret"
```

### 示例 3: 获取机密值

```bash
az keyvault secret show --vault-name my-vault --name db-password
```

### 示例 4: 创建自签名证书

```bash
az keyvault certificate create --vault-name my-vault --name my-cert --policy "$(az keyvault certificate get-default-policy)"
```

## 关联命令

- [[az-group|az group]]
- [[vault|vault]]

## 风险提示

> ⚠️ **HIGH**: 密钥和机密为敏感信息，操作需严格权限控制

## 所属维度

[[Azure CLI-MOC|云平台/Azure CLI]]
