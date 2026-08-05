---
{
  "cmd_name": "systemctl cat",
  "cmd_category": "操作系统/Systemd服务管理",
  "cmd_dimension": "Systemd服务管理",
  "cmd_install": "Linux 系统自带 (systemd)",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "systemctl edit"
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

# systemctl cat

> 查看服务单元文件完整配置

## 安装

```bash
Linux 系统自带 (systemd)
```

## 用法

```
systemctl cat <service>
```

## 示例

### 示例 1: 查看 nginx 单元文件内容

```bash
systemctl cat nginx
```

### 示例 2: 查看 docker 完整 unit 配置

```bash
systemctl cat docker.service
```

## 关联命令

- [[systemctl-edit|systemctl edit]]

## 风险提示

> ⚠️ **LOW**: 只读操作，无风险

## 最佳实践

[[bp-systemctl-cat|systemctl cat 生产环境最佳实践]]

## 所属维度

[[Systemd服务管理-MOC|操作系统/Systemd服务管理]]
