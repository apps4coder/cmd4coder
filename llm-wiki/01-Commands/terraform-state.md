---
{
  "cmd_name": "terraform state",
  "cmd_category": "云平台/配置管理",
  "cmd_dimension": "配置管理",
  "cmd_install": "同 terraform",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "terraform apply",
    "terraform import"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/config-mgmt.yaml"
}
---

# terraform state

> 管理 Terraform 状态文件

## 安装

```bash
同 terraform
```

## 用法

```
terraform state [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `-state` | 指定状态文件路径 |
| `-backup` | 备份文件路径 |

## 示例

### 示例 1: 列出状态中所有资源

```bash
terraform state list
```

### 示例 2: 查看资源状态详情

```bash
terraform state show aws_instance.web
```

### 示例 3: 重命名状态中的资源

```bash
terraform state mv aws_instance.old aws_instance.new
```

### 示例 4: 从状态中移除资源（不销毁实际资源）

```bash
terraform state rm aws_instance.orphan
```

## 关联命令

- [[terraform-apply|terraform apply]]
- [[terraform-import|terraform import]]

## 风险提示

> ⚠️ **HIGH**: state rm 导致资源脱离管理，state mv 错误可能丢失追踪

## 所属维度

[[配置管理-MOC|云平台/配置管理]]
