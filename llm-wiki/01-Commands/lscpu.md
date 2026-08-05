---
{
  "cmd_name": "lscpu",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lspci",
    "lsusb"
  ],
  "cmd_tags": [
    "architecture",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/os/linux-core.yaml"
}
---

# lscpu

> 显示 CPU 架构与信息

## 用法

```
lscpu [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-e` | 表格输出 |
| `-p` | 解析格式 |
| `-a` | 在线与离线 CPU |

## 示例

### 示例 1: 显示 CPU 信息

```bash
lscpu
```

### 示例 2: 表格显示每个 CPU

```bash
lscpu -e
```

## 关联命令

- [[lspci|lspci]]
- [[lsusb|lsusb]]

## 风险提示

> ⚠️ **LOW**: 命令风险较低，执行前请阅读文档并确认参数。

## 最佳实践

[[bp-lscpu|lscpu 生产环境最佳实践]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
