---
{
  "cmd_name": "istioctl",
  "cmd_category": "网络工具/服务网格",
  "cmd_dimension": "服务网格",
  "cmd_install": "curl -L https://istio.io/downloadIstio | sh - (或 brew install istioctl)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kubectl",
    "istioctl analyze"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/network/service-mesh.yaml"
}
---

# istioctl

> Istio 服务网格管理 CLI

## 安装

```bash
curl -L https://istio.io/downloadIstio | sh - (或 brew install istioctl)
```

## 用法

```
istioctl <命令>
```

```
istioctl install [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--set` | 设置安装参数 (--set profile=demo) |
| `-f` | 指定 IstioOperator 配置文件 |
| `--context` | 指定 kubeconfig context |
| `-n` | 指定命名空间 |

## 示例

### 示例 1: 安装 Istio demo 配置

```bash
istioctl install --set profile=demo -y
```

### 示例 2: 查看 Istio 版本

```bash
istioctl version
```

### 示例 3: 查看所有 sidecar 代理同步状态

```bash
istioctl proxy-status
```

### 示例 4: 按配置文件升级 Istio

```bash
istioctl upgrade -f istio-operator.yaml
```

## 关联命令

- [[kubectl|kubectl]]
- [[istioctl-analyze|istioctl analyze]]

## 风险提示

> ⚠️ **HIGH**: install/upgrade/uninstall 影响整个网格基础设施

## 最佳实践

[[bp-istioctl|istioctl 生产环境最佳实践]]

## 所属维度

[[服务网格-MOC|网络工具/服务网格]]
