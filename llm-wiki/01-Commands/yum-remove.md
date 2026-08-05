---
{
  "cmd_name": "yum remove",
  "cmd_category": "Operating System",
  "cmd_dimension": "Operating System",
  "cmd_install": "Pre-installed on CentOS/RHEL",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/os/centos.yaml"
}
---

# yum remove

> Remove installed packages

## 安装

```bash
Pre-installed on CentOS/RHEL
```

## 用法

```
sudo yum remove <package>
```

## 示例

### 示例 1: Remove nginx package

```bash
sudo yum remove nginx
```

### 示例 2: 无需确认移除包

```bash
sudo yum remove -y nginx
```

## 风险提示

> ⚠️ **HIGH**: Removing system packages may break system

> ⚠️ **HIGH**: 操作前建议确认目标对象，并在非生产环境验证后再执行。

## 最佳实践

[[bp-yum-remove|yum remove 生产环境最佳实践]]

## 所属维度

[[Operating System-MOC|Operating System]]
