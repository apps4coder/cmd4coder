---
{
  "cmd_name": "systemctl status prometheus",
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

# systemctl status prometheus

> Check Prometheus service status

## 安装

```bash
Built-in systemd command
```

## 用法

```
systemctl status prometheus
```

## 示例

### 示例 1: View Prometheus service status

```bash
systemctl status prometheus
```

### 示例 2: Start Prometheus service

```bash
systemctl start prometheus
```

### 示例 3: Restart Prometheus service

```bash
systemctl restart prometheus
```

## 风险提示

> ⚠️ **LOW**: Read-only status check; no risks

> ⚠️ **MEDIUM**: Restarting Prometheus causes brief monitoring gap

## 最佳实践

[[bp-systemctl-status-prometheus|systemctl status prometheus 生产环境最佳实践]]

## 所属维度

[[Kubernetes Monitoring  Logging-MOC|Kubernetes Monitoring & Logging]]
