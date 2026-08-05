---
{
  "cmd_name": "gh issue",
  "cmd_category": "版本控制/Git高级操作",
  "cmd_dimension": "Git高级操作",
  "cmd_install": "同 gh",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "gh pr",
    "gh release"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/vcs/git-advanced.yaml"
}
---

# gh issue

> GitHub CLI Issue 管理

## 安装

```bash
同 gh
```

## 用法

```
gh issue [命令] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `create` | 创建 Issue |
| `list` | 列出 Issue |
| `close` | 关闭 Issue |
| `comment` | 添加评论 |
| `-l` | 标签过滤 |

## 示例

### 示例 1: 创建带标签的 Issue

```bash
gh issue create --title "Bug: login fails" --body "Steps to reproduce..." --label bug
```

### 示例 2: 列出打开的 bug

```bash
gh issue list --label bug --state open
```

### 示例 3: 关闭并评论

```bash
gh issue close 42 --comment "Fixed in v2.1.0"
```

### 示例 4: 查看 Issue 及评论

```bash
gh issue view 42 --comments
```

## 关联命令

- [[gh-pr|gh pr]]
- [[gh-release|gh release]]

## 风险提示

> ⚠️ **LOW**: Issue 操作风险低，close 可重新打开

## 最佳实践

[[bp-gh-issue|gh issue 生产环境最佳实践]]

## 所属维度

[[Git高级操作-MOC|版本控制/Git高级操作]]
