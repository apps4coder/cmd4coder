---
{
  "cmd_name": "xxd",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "od",
    "hexdump"
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

# xxd

> 十六进制查看器和编辑器

## 用法

```
xxd [OPTIONS] [FILE]
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | 限制长度 |
| `-s` | 跳过偏移 |
| `-p` | 纯十六进制 |
| `-r` | 反向转换 |

## 示例

### 示例 1: 查看二进制文件

```bash
xxd file.bin | head
```

### 示例 2: 输出纯十六进制

```bash
xxd -p file.bin
```

## 风险提示

> ⚠️ **LOW**: 命令风险较低，执行前请阅读文档并确认参数。

## 最佳实践

[[bp-xxd|xxd 生产环境最佳实践]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
