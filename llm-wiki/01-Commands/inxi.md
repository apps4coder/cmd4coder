---
{
  "cmd_name": "inxi",
  "cmd_category": "硬件/系统信息",
  "cmd_dimension": "系统信息",
  "cmd_install": "包管理器安装，如 sudo apt install inxi",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lshw",
    "hardinfo"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/hardware/info.yaml"
}
---

# inxi

> 友好的系统/硬件信息汇总工具

## 安装

```bash
包管理器安装，如 sudo apt install inxi
```

## 用法

```
inxi [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-F` | 完整输出 |
| `-G` | 显卡 |
| `-N` | 网络 |
| `-D` | 硬盘 |
| `-z` | 隐藏敏感 |

## 示例

### 示例 1: 完整系统信息

```bash
inxi -F
```

### 示例 2: 显卡信息

```bash
inxi -G
```

## 关联命令

- [[lshw|lshw]]
- [[hardinfo|hardinfo]]

## 风险提示

> ⚠️ **LOW**: 只读/信息查询类操作，风险较低，但仍需确认目标对象与权限。

## 最佳实践

[[bp-inxi|inxi 生产环境最佳实践]]

## 所属维度

[[系统信息-MOC|硬件/系统信息]]
