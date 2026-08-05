---
{
  "cmd_name": "tkn",
  "cmd_category": "CI-CD/平台工具",
  "cmd_dimension": "平台工具",
  "cmd_install": "brew install tektoncd-cli (macOS) 或 apt install tektoncd-cli",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "tkn pipeline start",
    "kubectl"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cicd/platforms.yaml"
}
---

# tkn

> Tekton CLI，管理云原生 CI/CD Pipeline

## 安装

```bash
brew install tektoncd-cli (macOS) 或 apt install tektoncd-cli
```

## 用法

```
tkn [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 命名空间 |
| `--context` | kubeconfig context |

## 示例

### 示例 1: 列出 Pipeline 定义

```bash
tkn pipeline list
```

### 示例 2: 列出 Pipeline 运行记录

```bash
tkn pipelinerun list
```

### 示例 3: 实时查看运行日志

```bash
tkn pipelinerun logs -f
```

### 示例 4: 列出 Task 定义

```bash
tkn task list
```

## 关联命令

- [[tkn-pipeline-start|tkn pipeline start]]
- [[kubectl|kubectl]]

## 风险提示

> ⚠️ **LOW**: 查看操作无风险

## 最佳实践

[[bp-tkn|tkn 生产环境最佳实践]]

## 所属维度

[[平台工具-MOC|CI-CD/平台工具]]
