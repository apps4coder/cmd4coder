---
{
  "cmd_name": "systemctl timer",
  "cmd_category": "操作系统/Systemd服务管理",
  "cmd_dimension": "Systemd服务管理",
  "cmd_install": "Linux 系统自带 (systemd)",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "systemd-run",
    "crontab"
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

# systemctl timer

> 管理 systemd 定时器（替代 cron）

## 安装

```bash
Linux 系统自带 (systemd)
```

## 用法

```
systemctl list-timers
```

```
systemctl start <name>.timer
```

```
systemctl enable <name>.timer
```

## 参数

| Flag | Description |
|------|-------------|
| `--all` | 显示所有定时器（含未激活） |
| `--user` | 操作用户级定时器 |

## 示例

### 示例 1: 列出所有定时器及下次触发时间

```bash
systemctl list-timers --all
```

### 示例 2: 启用磁盘 TRIM 定时器

```bash
systemctl enable --now fstrim.timer
```

### 示例 3: 查看日志轮转定时器状态

```bash
systemctl status logrotate.timer
```

## 关联命令

- [[systemd-run|systemd-run]]
- [[crontab|crontab]]

## 风险提示

> ⚠️ **LOW**: 定时器管理操作风险较低

## 最佳实践

[[bp-systemctl-timer|systemctl timer 生产环境最佳实践]]

## 所属维度

[[Systemd服务管理-MOC|操作系统/Systemd服务管理]]
