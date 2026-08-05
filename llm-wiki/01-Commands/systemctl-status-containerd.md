---
{
  "cmd_name": "systemctl status containerd",
  "cmd_category": "Kubernetes Container Runtime",
  "cmd_dimension": "Kubernetes Container Runtime",
  "cmd_install": "Built-in systemd command",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/container/k8s/k8s-runtime.yaml"
}
---

# systemctl status containerd

> Check containerd service status

## 安装

```bash
Built-in systemd command
```

## 用法

```
systemctl status containerd
```

## 示例

### 示例 1: View containerd service status

```bash
systemctl status containerd
```

### 示例 2: Start containerd service

```bash
systemctl start containerd
```

### 示例 3: Enable containerd to start on boot

```bash
systemctl enable containerd
```

### 示例 4: Restart containerd service

```bash
systemctl restart containerd
```

## 风险提示

> ⚠️ **LOW**: Read-only status check; no risks

> ⚠️ **HIGH**: Restarting containerd affects all running containers

## 最佳实践

[[bp-systemctl-status-containerd|systemctl status containerd 生产环境最佳实践]]

## 所属维度

[[Kubernetes Container Runtime-MOC|Kubernetes Container Runtime]]
