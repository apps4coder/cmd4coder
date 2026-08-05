---
{
  "cmd_name": "systemctl",
  "cmd_category": "操作系统/Systemd服务管理",
  "cmd_dimension": "Systemd服务管理",
  "cmd_install": "Linux 系统自带 (systemd)",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "journalctl",
    "systemd-analyze"
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

# systemctl

> 管理系统服务、套接字、挂载单元等

## 安装

```bash
Linux 系统自带 (systemd)
```

## 用法

```
systemctl <命令> [单元名]
```

```
systemctl <start|stop|restart|status> <service>
```

## 参数

| Flag | Description |
|------|-------------|
| `--now` | enable/disable 时同时启动/停止服务 |
| `-u` | 指定用户级服务 (--user) |
| `-t` | 按单元类型过滤 (service/socket/timer) |
| `--failed` | 列出失败的单元 |
| `-l` | 显示完整输出不截断 |

## 示例

### 示例 1: 查看 nginx 服务状态

```bash
systemctl status nginx
```

### 示例 2: 设置开机启动并立即启动 docker

```bash
systemctl enable --now docker
```

### 示例 3: 列出所有运行中的服务

```bash
systemctl list-units -t service --state running
```

### 示例 4: 重新加载 systemd 配置

```bash
systemctl daemon-reload
```

### 示例 5: 彻底禁用服务（无法手动启动）

```bash
systemctl mask firewalld
```

## 关联命令

- [[journalctl|journalctl]]
- [[systemd-analyze|systemd-analyze]]

## 风险提示

> ⚠️ **MEDIUM**: stop/disable/mask 可能中断关键服务

## 最佳实践

[[bp-systemctl|systemctl 生产环境最佳实践]]

## 所属维度

[[Systemd服务管理-MOC|操作系统/Systemd服务管理]]
