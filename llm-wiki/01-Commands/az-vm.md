---
{
  "cmd_name": "az vm",
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
    "az network"
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

# az vm

> 管理 Azure 虚拟机

## 安装

```bash
同 az
```

## 用法

```
az vm [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--name` | 虚拟机名称 |
| `--resource-group` | 所属资源组 |
| `--size` | VM 规格 (Standard_B2s/Standard_D2s_v3) |
| `--image` | 操作系统镜像 (UbuntuLTS/Win2022Datacenter) |
| `--admin-username` | 管理员用户名 |

## 示例

### 示例 1: 列出资源组内虚拟机

```bash
az vm list --resource-group my-rg --output table
```

### 示例 2: 创建 Linux 虚拟机

```bash
az vm create --resource-group my-rg --name my-vm --image UbuntuLTS --size Standard_B2s --admin-username azureuser --generate-ssh-keys
```

### 示例 3: 启动虚拟机

```bash
az vm start --resource-group my-rg --name my-vm
```

### 示例 4: 停止并释放计算资源（停止计费）

```bash
az vm deallocate --resource-group my-rg --name my-vm
```

## 关联命令

- [[az-group|az group]]
- [[az-network|az network]]

## 风险提示

> ⚠️ **HIGH**: VM 运行产生持续费用，delete 操作不可逆

## 所属维度

[[Azure CLI-MOC|云平台/Azure CLI]]
