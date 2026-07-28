---
{
  "cmd_name": "linkerd viz",
  "cmd_category": "网络工具/服务网格",
  "cmd_dimension": "服务网格",
  "cmd_install": "linkerd viz install | kubectl apply -f -",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "linkerd",
    "linkerd jaeger"
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

# linkerd viz

> Linkerd 可观测性面板与指标

## 安装

```bash
linkerd viz install | kubectl apply -f -
```

## 用法

```
linkerd viz <命令>
```

```
linkerd viz dashboard
```

## 示例

### 示例 1: 打开 Linkerd Web 面板

```bash
linkerd viz dashboard
```

### 示例 2: 查看部署的实时流量指标

```bash
linkerd viz stat deploy -n myapp
```

### 示例 3: 实时查看请求 top 列表

```bash
linkerd viz top deploy/myapp
```

### 示例 4: 实时查看请求流（类似 tcpdump）

```bash
linkerd viz tap deploy/myapp
```

### 示例 5: 查看服务间连接关系

```bash
linkerd viz edges deploy
```

## 关联命令

- [[linkerd|linkerd]]

## 风险提示

> ⚠️ **LOW**: 只读可观测性操作

## 所属维度

[[服务网格-MOC|网络工具/服务网格]]
