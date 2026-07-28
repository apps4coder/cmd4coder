---
{
  "cmd_name": "ansible-galaxy",
  "cmd_category": "云平台/配置管理",
  "cmd_dimension": "配置管理",
  "cmd_install": "同 ansible",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ansible",
    "ansible-playbook"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/config-mgmt.yaml"
}
---

# ansible-galaxy

> 管理 Ansible 社区角色和集合

## 安装

```bash
同 ansible
```

## 用法

```
ansible-galaxy [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `-r` | 从 requirements.yml 安装 |
| `-p` | 指定安装路径 |

## 示例

### 示例 1: 安装社区 Docker 角色

```bash
ansible-galaxy install geerlingguy.docker
```

### 示例 2: 批量安装依赖角色

```bash
ansible-galaxy install -r requirements.yml
```

### 示例 3: 安装集合

```bash
ansible-galaxy collection install community.general
```

### 示例 4: 列出已安装角色

```bash
ansible-galaxy role list
```

## 关联命令

- [[ansible|ansible]]
- [[ansible-playbook|ansible-playbook]]

## 风险提示

> ⚠️ **LOW**: 仅安装第三方代码，需审查来源可信度

## 所属维度

[[配置管理-MOC|云平台/配置管理]]
