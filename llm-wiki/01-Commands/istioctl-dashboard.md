---
{
  "cmd_name": "istioctl dashboard",
  "cmd_category": "网络工具/服务网格",
  "cmd_dimension": "服务网格",
  "cmd_install": "curl -L https://istio.io/downloadIstio | sh -",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "istioctl",
    "kubectl port-forward"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/network/service-mesh.yaml"
}
---

# istioctl dashboard

> 打开 Istio 相关 Web 控制台

## 安装

```bash
curl -L https://istio.io/downloadIstio | sh -
```

## 用法

```
istioctl dashboard <名称>
```

## 示例

### 示例 1: 打开 Kiali 服务拓扑面板

```bash
istioctl dashboard kiali
```

### 示例 2: 打开 Grafana 监控面板

```bash
istioctl dashboard grafana
```

### 示例 3: 打开 Jaeger 链路追踪

```bash
istioctl dashboard jaeger
```

### 示例 4: 打开 Prometheus 查询界面

```bash
istioctl dashboard prometheus
```

## 关联命令

- [[istioctl|istioctl]]
- [[kubectl-port-forward|kubectl port-forward]]

## 风险提示

> ⚠️ **LOW**: 仅打开本地端口转发

## 所属维度

[[服务网格-MOC|网络工具/服务网格]]
