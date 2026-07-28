---
{
  "cmd_name": "flux reconcile",
  "cmd_category": "CI-CD/GitOps",
  "cmd_dimension": "GitOps",
  "cmd_install": "同 flux",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "flux create kustomization",
    "flux get kustomizations"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cicd/gitops.yaml"
}
---

# flux reconcile

> 手动触发 Flux 资源同步（不等待轮询间隔）

## 安装

```bash
同 flux
```

## 用法

```
flux reconcile [类型] [名称] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--with-source` | 同时拉取最新源 |
| `--force` | 强制同步（忽略漂移检测） |

## 示例

### 示例 1: 拉取最新代码并同步

```bash
flux reconcile kustomization my-app --with-source
```

### 示例 2: 仅拉取最新 Git 源

```bash
flux reconcile source git my-app
```

### 示例 3: 强制重新部署 Helm Release

```bash
flux reconcile helmrelease my-chart --force
```

### 示例 4: 同步所有 Kustomization

```bash
flux reconcile kustomization --all
```

## 关联命令

- [[flux-create-kustomization|flux create kustomization]]
- [[flux-get-kustomizations|flux get kustomizations]]

## 风险提示

> ⚠️ **MEDIUM**: 立即触发部署，绕过正常轮询节奏

## 所属维度

[[GitOps-MOC|CI-CD/GitOps]]
