---
{
  "cmd_name": "az group",
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
    "az",
    "az vm"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/azure.yaml"
}
---

# az group

> 管理 Azure 资源组（资源逻辑容器）

## 安装

```bash
同 az
```

## 用法

```
az group [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--name` | 资源组名称 |
| `--location` | 区域 (eastus/westus2/eastasia) |
| `--tags` | 标签 (key=value) |

## 示例

### 示例 1: 创建资源组

```bash
az group create --name my-rg --location eastus
```

### 示例 2: 列出所有资源组

```bash
az group list --output table
```

### 示例 3: 查看资源组详情

```bash
az group show --name my-rg
```

### 示例 4: 删除资源组及其所有资源

```bash
az group delete --name my-rg --yes
```

## 关联命令

- [[az|az]]
- [[az-vm|az vm]]

## 风险提示

> ⚠️ **CRITICAL**: group delete 会删除资源组内所有资源，操作不可逆

## 最佳实践

[[bp-az-group|az group 生产环境最佳实践]]

## 所属维度

[[Azure CLI-MOC|云平台/Azure CLI]]
