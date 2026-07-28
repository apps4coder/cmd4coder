---
{
  "cmd_name": "flux create source",
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
    "flux get sources"
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

# flux create source

> 创建 Flux 源（Git 仓库、Helm 仓库、OCI 仓库）

## 安装

```bash
同 flux
```

## 用法

```
flux create source git [名称] [选项]
```

```
flux create source helm [名称] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--url` | 仓库 URL |
| `--branch` | Git 分支 |
| `--interval` | 轮询间隔 (1m/5m/10m) |
| `--secret-ref` | 认证密钥引用 |

## 示例

### 示例 1: 创建 Git 源，5 分钟轮询

```bash
flux create source git my-app --url=https://github.com/org/repo --branch=main --interval=5m
```

### 示例 2: 创建 Helm 仓库源

```bash
flux create source helm bitnami --url=https://charts.bitnami.com/bitnami --interval=30m
```

### 示例 3: 使用 SSH 密钥创建私有仓库源

```bash
flux create source git my-app --url=ssh://git@github.com/org/repo --branch=prod --secret-ref=ssh-creds
```

## 关联命令

- [[flux-create-kustomization|flux create kustomization]]

## 风险提示

> ⚠️ **LOW**: 仅创建源定义，不直接修改工作负载

## 所属维度

[[GitOps-MOC|CI-CD/GitOps]]
