---
{
  "cmd_name": "argocd create",
  "cmd_category": "CI-CD/GitOps",
  "cmd_dimension": "GitOps",
  "cmd_install": "同 argocd",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "argocd app sync",
    "argocd app delete"
  ],
  "cmd_tags": [
    "application",
    "kubernetes",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cicd/gitops.yaml"
}
---

# argocd create

> 在 ArgoCD 中创建应用（关联 Git 仓库与 K8s 集群）

## 安装

```bash
同 argocd
```

## 用法

```
argocd app create [应用名] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--repo` | Git 仓库 URL |
| `--path` | 仓库中 manifests 路径 |
| `--dest-server` | 目标集群 API 地址 |
| `--dest-namespace` | 目标命名空间 |
| `--sync-policy` | 同步策略 (automated/manual) |
| `--auto-prune` | 自动清理已删除资源 |

## 示例

### 示例 1: 创建手动同步应用

```bash
argocd app create my-app --repo https://github.com/org/repo --path k8s/ --dest-server https://kubernetes.default.svc --dest-namespace production
```

### 示例 2: 创建自动同步+自动修剪应用

```bash
argocd app create my-app --repo https://github.com/org/repo --path k8s/ --dest-namespace default --sync-policy automated --auto-prune
```

### 示例 3: 创建 Helm 应用指定 values

```bash
argocd app create my-app --repo https://github.com/org/repo --path helm/ --dest-namespace default --helm-values values-prod.yaml
```

## 关联命令

- [[argocd-app-sync|argocd app sync]]
- [[argocd-app-delete|argocd app delete]]

## 风险提示

> ⚠️ **MEDIUM**: automated + auto-prune 会自动删除 Git 中不存在的资源

## 所属维度

[[GitOps-MOC|CI-CD/GitOps]]
