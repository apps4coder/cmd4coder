---
{
  "cmd_name": "az bicep",
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
    "terraform"
  ],
  "cmd_tags": [
    "deployment",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/azure.yaml"
}
---

# az bicep

> Azure Bicep 基础设施即代码部署

## 安装

```bash
同 az
```

## 用法

```
az deployment group create [参数]
```

```
az bicep [命令]
```

## 参数

| Flag | Description |
|------|-------------|
| `--template-file` | Bicep 模板文件路径 |
| `--parameters` | 参数文件或直接参数 |
| `--resource-group` | 目标资源组 |

## 示例

### 示例 1: 安装 Bicep CLI

```bash
az bicep install
```

### 示例 2: 编译 Bicep 为 ARM JSON

```bash
az bicep build --file main.bicep
```

### 示例 3: 部署 Bicep 模板到资源组

```bash
az deployment group create --resource-group my-rg --template-file main.bicep --parameters env=prod
```

### 示例 4: 预览部署变更（不实际执行）

```bash
az deployment group what-if --resource-group my-rg --template-file main.bicep
```

## 关联命令

- [[az-group|az group]]
- [[terraform|terraform]]

## 风险提示

> ⚠️ **HIGH**: 部署可能创建/修改/删除资源，建议先用 what-if 预览

## 所属维度

[[Azure CLI-MOC|云平台/Azure CLI]]
