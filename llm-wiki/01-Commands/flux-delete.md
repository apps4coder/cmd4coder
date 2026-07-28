---
{
  "cmd_name": "flux delete",
  "cmd_category": "CI-CD/GitOps",
  "cmd_dimension": "GitOps",
  "cmd_install": "同 flux",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "flux create kustomization",
    "flux reconcile"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cicd/gitops.yaml"
}
---

# flux delete

> 删除 Flux 资源

## 安装

```bash
同 flux
```

## 用法

```
flux delete [类型] [名称] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--silent` | 跳过确认 |
| `--keep` | 保留集群中已部署的资源 |

## 示例

### 示例 1: 删除 Kustomization（含集群资源）

```bash
flux delete kustomization my-app
```

### 示例 2: 删除源但保留已部署资源

```bash
flux delete source git my-app --keep
```

### 示例 3: 无确认删除 Helm Release

```bash
flux delete helmrelease my-chart --silent
```

## 关联命令

- [[flux-create-kustomization|flux create kustomization]]
- [[flux-reconcile|flux reconcile]]

## 风险提示

> ⚠️ **HIGH**: 默认会删除关联的集群资源，--keep 可保留

## 所属维度

[[GitOps-MOC|CI-CD/GitOps]]
