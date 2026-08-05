---
{
  "cmd_name": "buildkite-agent",
  "cmd_category": "CI-CD/平台工具",
  "cmd_dimension": "平台工具",
  "cmd_install": "brew install buildkite/buildkite/buildkite-agent (macOS) 或参见 buildkite.com/docs",
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
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cicd/platforms.yaml"
}
---

# buildkite-agent

> Buildkite CI 代理，在自有基础设施运行构建

## 安装

```bash
brew install buildkite/buildkite/buildkite-agent (macOS) 或参见 buildkite.com/docs
```

## 用法

```
buildkite-agent [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--token` | Agent 注册令牌 |
| `--tags` | Agent 标签 (os=linux,queue=default) |

## 示例

### 示例 1: 启动 Agent 注册到 Buildkite

```bash
buildkite-agent start --token $BUILDKITE_TOKEN
```

### 示例 2: 上传动态 Pipeline 定义

```bash
buildkite-agent pipeline upload .buildkite/pipeline.yml
```

### 示例 3: 上传构建产物

```bash
buildkite-agent artifact upload "dist/*.tar.gz"
```

### 示例 4: 下载构建产物

```bash
buildkite-agent artifact download "dist/app" ./
```

## 关联命令

- [[gh-workflow|gh workflow]]
- [[act|act]]

## 风险提示

> ⚠️ **MEDIUM**: Agent 执行任意构建命令，确保安全隔离

## 最佳实践

[[bp-buildkite-agent|buildkite-agent 生产环境最佳实践]]

## 所属维度

[[平台工具-MOC|CI-CD/平台工具]]
