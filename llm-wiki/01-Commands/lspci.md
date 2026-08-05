---
{
  "cmd_name": "lspci",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lsusb",
    "lscpu"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/os/linux-core.yaml"
}
---

# lspci

> 列出 PCI 设备

## 用法

```
lspci [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-v` | 详细 |
| `-k` | 显示内核驱动 |
| `-nn` | 显示厂商 ID |

## 示例

### 示例 1: 列出 PCI 设备

```bash
lspci
```

### 示例 2: 查看网卡驱动

```bash
lspci -k | grep -A3 Ethernet
```

## 关联命令

- [[lsusb|lsusb]]
- [[lscpu|lscpu]]

## 风险提示

> ⚠️ **LOW**: 命令风险较低，执行前请阅读文档并确认参数。

## 最佳实践

[[bp-lspci|lspci 生产环境最佳实践]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
