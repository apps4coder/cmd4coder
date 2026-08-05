---
{
  "cmd_name": "systemd-analyze",
  "cmd_category": "操作系统/Systemd服务管理",
  "cmd_dimension": "Systemd服务管理",
  "cmd_install": "Linux 系统自带 (systemd)",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "systemctl"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/os/systemd.yaml"
}
---

# systemd-analyze

> 分析系统启动性能

## 安装

```bash
Linux 系统自带 (systemd)
```

## 用法

```
systemd-analyze [命令]
```

```
systemd-analyze blame
```

```
systemd-analyze critical-chain
```

## 参数

| Flag | Description |
|------|-------------|
| `--user` | 分析用户会话而非系统 |

## 示例

### 示例 1: 显示总启动耗时

```bash
systemd-analyze
```

### 示例 2: 按启动耗时排序所有服务

```bash
systemd-analyze blame
```

### 示例 3: 显示 nginx 关键启动链

```bash
systemd-analyze critical-chain nginx
```

### 示例 4: 生成启动时序 SVG 图

```bash
systemd-analyze plot > boot.svg
```

## 关联命令

- [[systemctl|systemctl]]

## 风险提示

> ⚠️ **LOW**: 只读分析操作

## 最佳实践

[[bp-systemd-analyze|systemd-analyze 生产环境最佳实践]]

## 所属维度

[[Systemd服务管理-MOC|操作系统/Systemd服务管理]]
