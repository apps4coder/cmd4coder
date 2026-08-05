---
{
  "cmd_name": "linkerd diagnostics",
  "cmd_category": "网络工具/服务网格",
  "cmd_dimension": "服务网格",
  "cmd_install": "curl --proto '=https' --tlsv1.2 -sSfL https://run.linkerd.io/install | sh",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "linkerd",
    "linkerd viz"
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

# linkerd diagnostics

> Linkerd 诊断和调试工具

## 安装

```bash
curl --proto '=https' --tlsv1.2 -sSfL https://run.linkerd.io/install | sh
```

## 用法

```
linkerd diagnostics <命令>
```

## 示例

### 示例 1: 获取 pod 的代理指标

```bash
linkerd diagnostics proxy-metrics deploy/myapp
```

### 示例 2: 查看服务端点发现信息

```bash
linkerd diagnostics endpoints deploy/myapp
```

### 示例 3: 查看授权策略

```bash
linkerd diagnostics policy get deploy/myapp
```

## 关联命令

- [[linkerd|linkerd]]
- [[linkerd-viz|linkerd viz]]

## 风险提示

> ⚠️ **LOW**: 只读诊断操作

## 最佳实践

[[bp-linkerd-diagnostics|linkerd diagnostics 生产环境最佳实践]]

## 所属维度

[[服务网格-MOC|网络工具/服务网格]]
