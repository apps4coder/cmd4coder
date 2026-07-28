---
{
  "cmd_name": "az aks",
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
    "kubectl"
  ],
  "cmd_tags": [
    "kubernetes",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/azure.yaml"
}
---

# az aks

> 管理 Azure Kubernetes Service 集群

## 安装

```bash
同 az
```

## 用法

```
az aks [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--name` | 集群名称 |
| `--resource-group` | 资源组 |
| `--node-count` | 节点数量 |
| `--node-vm-size` | 节点 VM 规格 |
| `--kubernetes-version` | K8s 版本 |

## 示例

### 示例 1: 列出所有 AKS 集群

```bash
az aks list --output table
```

### 示例 2: 创建 3 节点 AKS 集群

```bash
az aks create --resource-group my-rg --name my-cluster --node-count 3
```

### 示例 3: 获取集群 kubeconfig

```bash
az aks get-credentials --resource-group my-rg --name my-cluster
```

### 示例 4: 扩容至 5 节点

```bash
az aks scale --resource-group my-rg --name my-cluster --node-count 5
```

## 关联命令

- [[az-vm|az vm]]
- [[kubectl|kubectl]]

## 风险提示

> ⚠️ **HIGH**: 集群操作涉及费用，scale/delete 影响运行中的工作负载

## 所属维度

[[Azure CLI-MOC|云平台/Azure CLI]]
