---
{
  "cmd_name": "flux logs",
  "cmd_category": "CI-CD/GitOps",
  "cmd_dimension": "GitOps",
  "cmd_install": "同 flux",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "flux get all",
    "flux reconcile"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cicd/gitops.yaml"
}
---

# flux logs

> 查看 Flux 控制器和资源同步日志

## 安装

```bash
同 flux
```

## 用法

```
flux logs [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--kind` | 资源类型 (Kustomization/HelmRelease/GitRepository) |
| `--name` | 资源名称 |
| `--level` | 日志级别 (info/error/debug) |
| `--follow` | 实时跟踪 |

## 示例

### 示例 1: 查看应用同步错误日志

```bash
flux logs --kind=Kustomization --name=my-app --level=error
```

### 示例 2: 实时查看所有 Flux 日志

```bash
flux logs --follow
```

### 示例 3: 查看 Helm Release 日志

```bash
flux logs --kind=HelmRelease --name=my-chart
```

## 关联命令

- [[flux-reconcile|flux reconcile]]

## 风险提示

> ⚠️ **LOW**: 只读操作，无风险

## 最佳实践

[[bp-flux-logs|flux logs 生产环境最佳实践]]

## 所属维度

[[GitOps-MOC|CI-CD/GitOps]]
