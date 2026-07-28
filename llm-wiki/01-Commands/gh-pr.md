---
{
  "cmd_name": "gh pr",
  "cmd_category": "版本控制/Git高级操作",
  "cmd_dimension": "Git高级操作",
  "cmd_install": "brew install gh (macOS) 或 apt install gh (Ubuntu)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "gh issue",
    "git push"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/vcs/git-advanced.yaml"
}
---

# gh pr

> GitHub CLI Pull Request 管理

## 安装

```bash
brew install gh (macOS) 或 apt install gh (Ubuntu)
```

## 用法

```
gh pr [命令] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `create` | 创建 PR |
| `list` | 列出 PR |
| `checkout` | 检出 PR 分支 |
| `merge` | 合并 PR |
| `review` | 审查 PR |

## 示例

### 示例 1: 创建 PR

```bash
gh pr create --title "feat: add auth" --body "Implements OAuth2 flow"
```

### 示例 2: 列出分配给我的 PR

```bash
gh pr list --state open --assignee @me
```

### 示例 3: 检出 PR

```bash
gh pr checkout 42
```

### 示例 4: Squash 合并并删除分支

```bash
gh pr merge 42 --squash --delete-branch
```

### 示例 5: 批准 PR

```bash
gh pr review 42 --approve
```

## 关联命令

- [[gh-issue|gh issue]]
- [[git-push|git push]]

## 风险提示

> ⚠️ **MEDIUM**: merge 操作不可逆，确认代码已审查

## 所属维度

[[Git高级操作-MOC|版本控制/Git高级操作]]
