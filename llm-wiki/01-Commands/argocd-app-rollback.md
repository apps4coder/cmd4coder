---
{
  "cmd_name": "argocd app rollback",
  "cmd_category": "CI-CD/GitOps",
  "cmd_dimension": "GitOps",
  "cmd_install": "同 argocd",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "argocd app sync",
    "argocd app history"
  ],
  "cmd_tags": [
    "application",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cicd/gitops.yaml"
}
---

# argocd app rollback

> 回滚 ArgoCD 应用到历史版本

## 安装

```bash
同 argocd
```

## 用法

```
argocd app rollback [应用名] [修订ID]
```

## 参数

| Flag | Description |
|------|-------------|
| `--prune` | 回滚时修剪多余资源 |

## 示例

### 示例 1: 查看应用部署历史

```bash
argocd app history my-app
```

### 示例 2: 回滚到修订 ID 3

```bash
argocd app rollback my-app 3
```

### 示例 3: 回滚并修剪多余资源

```bash
argocd app rollback my-app 3 --prune
```

## 关联命令

- [[argocd-app-sync|argocd app sync]]

## 风险提示

> ⚠️ **HIGH**: 回滚影响生产部署，确认目标修订正确

## 所属维度

[[GitOps-MOC|CI-CD/GitOps]]
