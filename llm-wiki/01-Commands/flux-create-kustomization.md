---
{
  "cmd_name": "flux create kustomization",
  "cmd_category": "CI-CD/GitOps",
  "cmd_dimension": "GitOps",
  "cmd_install": "同 flux",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "flux create source",
    "flux reconcile"
  ],
  "cmd_tags": [
    "deployment",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cicd/gitops.yaml"
}
---

# flux create kustomization

> 创建 Flux Kustomization（定义如何部署源中的 manifests）

## 安装

```bash
同 flux
```

## 用法

```
flux create kustomization [名称] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--source` | 关联的源 (GitRepository/name) |
| `--path` | manifests 路径 |
| `--prune` | 自动修剪已删除资源 |
| `--interval` | 同步间隔 |
| `--target-namespace` | 目标命名空间 |

## 示例

### 示例 1: 创建 Kustomization 自动同步

```bash
flux create kustomization my-app --source=GitRepository/my-app --path=./k8s --prune=true --interval=5m --target-namespace=production
```

### 示例 2: 创建基础设施同步

```bash
flux create kustomization infra --source=GitRepository/infra --path=./clusters/prod --prune=true --interval=10m
```

## 关联命令

- [[flux-create-source|flux create source]]
- [[flux-reconcile|flux reconcile]]

## 风险提示

> ⚠️ **MEDIUM**: prune=true 会自动删除 Git 中不存在的集群资源

## 所属维度

[[GitOps-MOC|CI-CD/GitOps]]
