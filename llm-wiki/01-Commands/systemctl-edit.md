---
{
  "cmd_name": "systemctl edit",
  "cmd_category": "操作系统/Systemd服务管理",
  "cmd_dimension": "Systemd服务管理",
  "cmd_install": "Linux 系统自带 (systemd)",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "systemctl cat",
    "systemctl daemon-reload"
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

# systemctl edit

> 创建 override 文件覆盖服务默认配置

## 安装

```bash
Linux 系统自带 (systemd)
```

## 用法

```
systemctl edit <service>
```

```
systemctl edit --full <service>
```

## 参数

| Flag | Description |
|------|-------------|
| `--full` | 编辑完整副本而非 override 片段 |
| `--force` | 单元不存在时创建新单元 |

## 示例

### 示例 1: 为 nginx 添加 override 配置

```bash
systemctl edit nginx
```

### 示例 2: 创建新的自定义服务单元

```bash
systemctl edit --force myapp.service
```

## 关联命令

- [[systemctl-cat|systemctl cat]]

## 风险提示

> ⚠️ **MEDIUM**: 错误配置可能导致服务无法启动

## 最佳实践

[[bp-systemctl-edit|systemctl edit 生产环境最佳实践]]

## 所属维度

[[Systemd服务管理-MOC|操作系统/Systemd服务管理]]
