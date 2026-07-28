---
{
  "cmd_name": "istioctl experimental",
  "cmd_category": "网络工具/服务网格",
  "cmd_dimension": "服务网格",
  "cmd_install": "curl -L https://istio.io/downloadIstio | sh -",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "istioctl"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/network/service-mesh.yaml"
}
---

# istioctl experimental

> Istio 实验性功能（Waypoint、ambient 模式等）

## 安装

```bash
curl -L https://istio.io/downloadIstio | sh -
```

## 用法

```
istioctl experimental <命令>
```

```
istioctl x <命令>
```

## 示例

### 示例 1: 为命名空间创建 ambient waypoint 代理

```bash
istioctl x waypoint apply -n myapp
```

### 示例 2: 查看 waypoint 代理状态

```bash
istioctl x waypoint status
```

### 示例 3: 升级前兼容性检查

```bash
istioctl x precheck
```

## 关联命令

- [[istioctl|istioctl]]

## 风险提示

> ⚠️ **MEDIUM**: 实验性功能 API 可能变更

## 所属维度

[[服务网格-MOC|网络工具/服务网格]]
