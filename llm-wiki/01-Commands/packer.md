---
{
  "cmd_name": "packer",
  "cmd_category": "云平台/配置管理",
  "cmd_dimension": "配置管理",
  "cmd_install": "brew install packer (macOS) 或 apt install packer (HashiCorp 仓库)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "terraform",
    "ansible"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/config-mgmt.yaml"
}
---

# packer

> HashiCorp Packer 自动化机器镜像构建工具

## 安装

```bash
brew install packer (macOS) 或 apt install packer (HashiCorp 仓库)
```

## 用法

```
packer [命令] [模板文件]
```

## 参数

| Flag | Description |
|------|-------------|
| `-var` | 传入变量 |
| `-var-file` | 变量文件 |
| `-only` | 仅构建指定 builder |
| `-force` | 强制重建（覆盖已有镜像） |

## 示例

### 示例 1: 初始化插件

```bash
packer init .
```

### 示例 2: 验证模板语法

```bash
packer validate template.pkr.hcl
```

### 示例 3: 构建机器镜像

```bash
packer build -var "version=1.2.3" template.pkr.hcl
```

### 示例 4: 仅构建 AWS AMI

```bash
packer build -only=amazon-ebs template.pkr.hcl
```

## 关联命令

- [[terraform|terraform]]
- [[ansible|ansible]]

## 风险提示

> ⚠️ **MEDIUM**: 构建过程会创建临时云资源（产生费用），-force 覆盖已有镜像

## 最佳实践

[[bp-packer|packer 生产环境最佳实践]]

## 所属维度

[[配置管理-MOC|云平台/配置管理]]
