---
{
  "cmd_name": "argocd",
  "cmd_category": "CI-CD/GitOps",
  "cmd_dimension": "GitOps",
  "cmd_install": "brew install argocd (macOS) 或 curl -sSL -o argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "argocd app",
    "kubectl"
  ],
  "cmd_tags": [
    "kubernetes",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cicd/gitops.yaml"
}
---

# argocd

> ArgoCD CLI，管理 Kubernetes GitOps 持续交付

## 安装

```bash
brew install argocd (macOS) 或 curl -sSL -o argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
```

## 用法

```
argocd [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--server` | ArgoCD API 服务器地址 |
| `--auth-token` | 认证令牌 |
| `--grpc-web` | 使用 gRPC-Web 协议（无需端口转发） |
| `--insecure` | 跳过 TLS 验证 |

## 示例

### 示例 1: 登录 ArgoCD 服务器

```bash
argocd login argocd.example.com --grpc-web
```

### 示例 2: 列出所有应用

```bash
argocd app list
```

### 示例 3: 查看应用同步状态

```bash
argocd app get my-app
```

### 示例 4: 查看客户端和服务端版本

```bash
argocd version
```

## 关联命令

- [[kubectl|kubectl]]

## 风险提示

> ⚠️ **MEDIUM**: 应用操作影响 K8s 集群中的实际部署

## 最佳实践

[[bp-argocd|argocd 生产环境最佳实践]]

## 所属维度

[[GitOps-MOC|CI-CD/GitOps]]
