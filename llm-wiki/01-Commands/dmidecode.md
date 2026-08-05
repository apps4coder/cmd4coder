---
{
  "cmd_name": "dmidecode",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lscpu",
    "lspci"
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

# dmidecode

> 从 DMI 表读取硬件信息

## 用法

```
dmidecode [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-t` | 指定类型 |
| `-s` | 指定字符串关键字 |
| `-q` | 安静模式 |

## 示例

### 示例 1: 查看内存信息

```bash
sudo dmidecode -t memory
```

### 示例 2: 查看序列号

```bash
sudo dmidecode -s system-serial-number
```

## 关联命令

- [[lscpu|lscpu]]
- [[lspci|lspci]]

## 风险提示

> ⚠️ **LOW**: 命令风险较低，执行前请阅读文档并确认参数。

## 最佳实践

[[bp-dmidecode|dmidecode 生产环境最佳实践]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
