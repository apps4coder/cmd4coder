---
{
  "cmd_name": "flux",
  "cmd_category": "CI-CD/GitOps",
  "cmd_dimension": "GitOps",
  "cmd_install": "brew install fluxcd/tap/flux (macOS) 或 curl -s https://fluxcd.io/install.sh | bash",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "flux create",
    "flux reconcile",
    "kubectl"
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

# flux

> Flux CD CLI，云原生 GitOps 持续交付工具

## 安装

```bash
brew install fluxcd/tap/flux (macOS) 或 curl -s https://fluxcd.io/install.sh | bash
```

## 用法

```
flux [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--namespace` | 目标命名空间（默认 flux-system） |
| `--context` | kubeconfig context |
| `--timeout` | 操作超时 |

## 示例

### 示例 1: 检查 Flux 组件健康状态

```bash
flux check
```

### 示例 2: 列出所有 Flux 资源

```bash
flux get all
```

### 示例 3: 查看 Flux 版本

```bash
flux version
```

### 示例 4: 在集群中安装 Flux

```bash
flux install
```

## 关联命令

- [[flux-reconcile|flux reconcile]]
- [[kubectl|kubectl]]

## 风险提示

> ⚠️ **MEDIUM**: 操作影响集群中的 GitOps 流水线

## 最佳实践

[[bp-flux|flux 生产环境最佳实践]]

## 所属维度

[[GitOps-MOC|CI-CD/GitOps]]
