---
{
  "cmd_name": "systemd-run",
  "cmd_category": "操作系统/Systemd服务管理",
  "cmd_dimension": "Systemd服务管理",
  "cmd_install": "Linux 系统自带 (systemd)",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "systemctl",
    "crontab"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/os/systemd.yaml"
}
---

# systemd-run

> 在临时 systemd 单元中运行命令

## 安装

```bash
Linux 系统自带 (systemd)
```

## 用法

```
systemd-run [选项] <命令>
```

```
systemd-run --on-calendar=<表达式> <命令>
```

## 参数

| Flag | Description |
|------|-------------|
| `--unit` | 指定临时单元名称 |
| `--on-calendar` | 按日历表达式调度执行 |
| `--on-active` | 延迟指定时间后执行 |
| `--scope` | 以 scope 而非 service 运行 |
| `-p` | 设置单元属性 (-p MemoryMax=512M) |

## 示例

### 示例 1: 30 分钟后重启 nginx

```bash
systemd-run --on-active=30min 'systemctl restart nginx'
```

### 示例 2: 每天凌晨 3 点执行备份

```bash
systemd-run --on-calendar='*-*-* 03:00:00' /usr/bin/backup.sh
```

### 示例 3: 限制内存 256M 运行训练任务

```bash
systemd-run -p MemoryMax=256M --unit=limited-task python train.py
```

## 关联命令

- [[systemctl|systemctl]]
- [[crontab|crontab]]

## 风险提示

> ⚠️ **MEDIUM**: 调度的命令会实际执行，注意权限

## 最佳实践

[[bp-systemd-run|systemd-run 生产环境最佳实践]]

## 所属维度

[[Systemd服务管理-MOC|操作系统/Systemd服务管理]]
