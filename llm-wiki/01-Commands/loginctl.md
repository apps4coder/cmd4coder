---
{
  "cmd_name": "loginctl",
  "cmd_category": "操作系统/Systemd服务管理",
  "cmd_dimension": "Systemd服务管理",
  "cmd_install": "Linux 系统自带 (systemd)",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "systemctl",
    "who"
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

# loginctl

> 管理用户登录会话

## 安装

```bash
Linux 系统自带 (systemd)
```

## 用法

```
loginctl [命令]
```

```
loginctl list-sessions
```

```
loginctl user-status <用户>
```

## 参数

| Flag | Description |
|------|-------------|
| `--no-legend` | 不显示表头（适合脚本） |

## 示例

### 示例 1: 列出所有登录会话

```bash
loginctl list-sessions
```

### 示例 2: 列出已登录用户

```bash
loginctl list-users
```

### 示例 3: 终止指定用户所有会话

```bash
loginctl terminate-user olduser
```

### 示例 4: 查看 deploy 用户会话详情

```bash
loginctl user-status deploy
```

## 关联命令

- [[systemctl|systemctl]]

## 风险提示

> ⚠️ **MEDIUM**: terminate-user 会强制断开用户会话

## 最佳实践

[[bp-loginctl|loginctl 生产环境最佳实践]]

## 所属维度

[[Systemd服务管理-MOC|操作系统/Systemd服务管理]]
