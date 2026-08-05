---
{
  "cmd_name": "glab",
  "cmd_category": "CI-CD/平台工具",
  "cmd_dimension": "平台工具",
  "cmd_install": "brew install glab (macOS) 或 apt install glab (GitLab 仓库)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "gh",
    "git"
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

# glab

> GitLab 官方命令行工具，管理 MR、Pipeline、Issue

## 安装

```bash
brew install glab (macOS) 或 apt install glab (GitLab 仓库)
```

## 用法

```
glab [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `-R` | 指定仓库 (group/project) |
| `--token` | 个人访问令牌 |

## 示例

### 示例 1: 列出打开的 Merge Request

```bash
glab mr list
```

### 示例 2: 创建 Merge Request

```bash
glab mr create --title "feat: add login" --source-branch feature/login --target-branch main
```

### 示例 3: 查看当前分支 Pipeline 状态

```bash
glab ci status
```

### 示例 4: 手动触发 Pipeline

```bash
glab ci run
```

## 关联命令

- [[gh|gh]]

## 风险提示

> ⚠️ **MEDIUM**: ci run 消耗 Runner 配额，mr merge 合并代码

## 最佳实践

[[bp-glab|glab 生产环境最佳实践]]

## 所属维度

[[平台工具-MOC|CI-CD/平台工具]]
