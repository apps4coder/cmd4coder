---
{
  "cmd_name": "drone",
  "cmd_category": "CI-CD/平台工具",
  "cmd_dimension": "平台工具",
  "cmd_install": "brew install drone-cli (macOS) 或 go install github.com/drone/drone-cli@latest",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "gh workflow",
    "act"
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

# drone

> Drone CI 命令行工具，管理构建和仓库

## 安装

```bash
brew install drone-cli (macOS) 或 go install github.com/drone/drone-cli@latest
```

## 用法

```
drone [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--server` | Drone 服务器地址 |
| `--token` | 个人访问令牌 |

## 示例

### 示例 1: 列出构建记录

```bash
drone build list org/repo
```

### 示例 2: 重启第 42 次构建

```bash
drone build restart org/repo 42
```

### 示例 3: 查看构建日志

```bash
drone build logs org/repo 42
```

### 示例 4: 启用仓库 CI

```bash
drone repo enable org/repo
```

### 示例 5: 本地执行 Pipeline

```bash
drone exec --pipeline build
```

## 关联命令

- [[gh-workflow|gh workflow]]
- [[act|act]]

## 风险提示

> ⚠️ **LOW**: 查看操作无风险，restart 消耗资源

## 最佳实践

[[bp-drone|drone 生产环境最佳实践]]

## 所属维度

[[平台工具-MOC|CI-CD/平台工具]]
