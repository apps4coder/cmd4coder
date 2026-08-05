---
{
  "cmd_name": "vault operator",
  "cmd_category": "云平台/配置管理",
  "cmd_dimension": "配置管理",
  "cmd_install": "同 vault",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "vault"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/config-mgmt.yaml"
}
---

# vault operator

> Vault 运维操作（初始化、解封、轮换）

## 安装

```bash
同 vault
```

## 用法

```
vault operator [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `-key-shares` | 密钥分片数 |
| `-key-threshold` | 解封所需分片数 |

## 示例

### 示例 1: 初始化 Vault（5 分片，3 个解封）

```bash
vault operator init -key-shares=5 -key-threshold=3
```

### 示例 2: 使用分片解封 Vault

```bash
vault operator unseal <unseal-key>
```

### 示例 3: 轮换加密密钥

```bash
vault operator rotate
```

### 示例 4: 重新封印 Vault

```bash
vault operator seal
```

## 关联命令

- [[vault|vault]]

## 风险提示

> ⚠️ **CRITICAL**: unseal key 丢失将导致数据永久不可访问，seal 会中断所有服务

## 最佳实践

[[bp-vault-operator|vault operator 生产环境最佳实践]]

## 所属维度

[[配置管理-MOC|云平台/配置管理]]
