---
{
  "cmd_name": "nvme",
  "cmd_category": "硬件/存储与RAID",
  "cmd_dimension": "存储与RAID",
  "cmd_install": "包管理器安装 nvme-cli",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "smartctl",
    "fio"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/hardware/storage.yaml"
}
---

# nvme

> NVMe 设备管理 CLI

## 安装

```bash
包管理器安装 nvme-cli
```

## 用法

```
nvme [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `list` | 列出设备 |
| `smart-log` | 智能日志 |
| `format` | 格式化 |
| `fw-log` |  |

## 示例

### 示例 1: 列出 NVMe 设备

```bash
sudo nvme list
```

### 示例 2: 查看 SMART 日志

```bash
sudo nvme smart-log /dev/nvme0
```

## 关联命令

- [[smartctl|smartctl]]
- [[fio|fio]]

## 风险提示

> ⚠️ **HIGH**: format 会清除所有数据，请确认目标设备

> ⚠️ **HIGH**: 操作前请仔细阅读文档并确认参数，建议在测试环境或非生产数据上先行验证。

## 最佳实践

[[bp-nvme|nvme 生产环境最佳实践]]

## 所属维度

[[存储与RAID-MOC|硬件/存储与RAID]]
