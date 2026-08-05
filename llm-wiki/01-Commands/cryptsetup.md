---
{
  "cmd_name": "cryptsetup",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "mkfs",
    "mount"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/os/linux-core.yaml"
}
---

# cryptsetup

> LUKS/dm-crypt 磁盘加密工具

## 用法

```
cryptsetup [OPTIONS] COMMAND [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `luksFormat` | 格式化 |
| `open` | 打开 |
| `close` | 关闭 |
| `status` | 状态 |

## 示例

### 示例 1: 创建 LUKS 加密分区

```bash
sudo cryptsetup luksFormat /dev/sdb1
```

### 示例 2: 打开加密映射

```bash
sudo cryptsetup open /dev/sdb1 secret
```

## 关联命令

- [[mkfs|mkfs]]
- [[mount|mount]]

## 风险提示

> ⚠️ **CRITICAL**: luksFormat 会擦除数据并加密，丢失密钥将导致数据永久不可恢复

> ⚠️ **CRITICAL**: 操作前请仔细阅读文档并确认参数，建议在测试环境或非生产数据上先行验证。

## 最佳实践

[[bp-cryptsetup|cryptsetup 生产环境最佳实践]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
