---
{
  "cmd_name": "az webapp",
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
    "az group",
    "az functionapp"
  ],
  "cmd_tags": [
    "application",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/azure.yaml"
}
---

# az webapp

> 管理 Azure App Service Web 应用

## 安装

```bash
同 az
```

## 用法

```
az webapp [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--name` | 应用名称 |
| `--resource-group` | 资源组 |
| `--plan` | App Service 计划 |
| `--runtime` | 运行时 (PYTHON:3.11/NODE:20-lts/DOTNETCORE:8.0) |

## 示例

### 示例 1: 列出所有 Web 应用

```bash
az webapp list --output table
```

### 示例 2: 创建 Python Web 应用

```bash
az webapp create --resource-group my-rg --plan my-plan --name my-app --runtime "PYTHON:3.11"
```

### 示例 3: 部署 ZIP 包

```bash
az webapp deployment source config-zip --resource-group my-rg --name my-app --src app.zip
```

### 示例 4: 实时查看应用日志

```bash
az webapp log tail --resource-group my-rg --name my-app
```

## 关联命令

- [[az-group|az group]]
- [[az-functionapp|az functionapp]]

## 风险提示

> ⚠️ **MEDIUM**: 部署会中断当前运行的应用

## 最佳实践

[[bp-az-webapp|az webapp 生产环境最佳实践]]

## 所属维度

[[Azure CLI-MOC|云平台/Azure CLI]]
