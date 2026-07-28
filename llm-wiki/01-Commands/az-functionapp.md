---
{
  "cmd_name": "az functionapp",
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
    "az webapp",
    "az storage"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/azure.yaml"
}
---

# az functionapp

> 管理 Azure Functions 无服务器计算

## 安装

```bash
同 az
```

## 用法

```
az functionapp [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--name` | 函数应用名 |
| `--resource-group` | 资源组 |
| `--consumption-plan-location` | 消费计划区域 |
| `--runtime` | 运行时 |

## 示例

### 示例 1: 列出函数应用

```bash
az functionapp list --output table
```

### 示例 2: 创建 Python 函数应用

```bash
az functionapp create --resource-group my-rg --consumption-plan-location eastus --name my-func --storage-account mystorage --runtime python
```

### 示例 3: 部署函数代码

```bash
az functionapp deployment source config-zip --resource-group my-rg --name my-func --src func.zip
```

### 示例 4: 查看函数密钥

```bash
az functionapp keys list --resource-group my-rg --name my-func
```

## 关联命令

- [[az-webapp|az webapp]]
- [[az-storage|az storage]]

## 风险提示

> ⚠️ **MEDIUM**: 密钥泄露可导致函数被未授权调用

## 所属维度

[[Azure CLI-MOC|云平台/Azure CLI]]
