---
{
  "cmd_name": "az network",
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
    "az vm",
    "az group"
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

# az network

> 管理 Azure 网络资源（VNet、NSG、负载均衡器）

## 安装

```bash
同 az
```

## 用法

```
az network [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--resource-group` | 资源组 |
| `--name` | 资源名称 |

## 示例

### 示例 1: 列出虚拟网络

```bash
az network vnet list --output table
```

### 示例 2: 创建虚拟网络

```bash
az network vnet create --resource-group my-rg --name my-vnet --address-prefix 10.0.0.0/16
```

### 示例 3: 创建 NSG 规则允许 SSH

```bash
az network nsg rule create --resource-group my-rg --nsg-name my-nsg --name allow-ssh --priority 100 --destination-port-ranges 22 --access Allow
```

### 示例 4: 创建公网 IP

```bash
az network public-ip create --resource-group my-rg --name my-ip
```

## 关联命令

- [[az-vm|az vm]]
- [[az-group|az group]]

## 风险提示

> ⚠️ **HIGH**: NSG 规则配置错误可能导致服务不可达或安全暴露

## 所属维度

[[Azure CLI-MOC|云平台/Azure CLI]]
