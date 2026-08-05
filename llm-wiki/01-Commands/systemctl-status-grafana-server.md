---
{
  "cmd_name": "systemctl status grafana-server",
  "cmd_category": "Kubernetes Monitoring & Logging",
  "cmd_dimension": "Kubernetes Monitoring  Logging",
  "cmd_install": "Built-in systemd command",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/container/k8s/k8s-monitor.yaml"
}
---

# systemctl status grafana-server

> Check Grafana service status

## 安装

```bash
Built-in systemd command
```

## 用法

```
systemctl status grafana-server
```

## 示例

### 示例 1: View Grafana service status

```bash
systemctl status grafana-server
```

### 示例 2: Start Grafana service

```bash
systemctl start grafana-server
```

### 示例 3: Restart Grafana service

```bash
systemctl restart grafana-server
```

## 风险提示

> ⚠️ **LOW**: Read-only status check; no risks

> ⚠️ **MEDIUM**: Restarting Grafana disrupts dashboard access

## 最佳实践

[[bp-systemctl-status-grafana-server|systemctl status grafana-server 生产环境最佳实践]]

## 所属维度

[[Kubernetes Monitoring  Logging-MOC|Kubernetes Monitoring & Logging]]
