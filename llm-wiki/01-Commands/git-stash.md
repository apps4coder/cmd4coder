---
{
  "cmd_name": "git stash",
  "cmd_category": "版本控制/Git高级操作",
  "cmd_dimension": "Git高级操作",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "git worktree",
    "git branch"
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

# git stash

> 暂存工作区变更（切换分支时保存未完成工作）

## 用法

```
git stash [命令] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `push` | 暂存变更 |
| `pop` | 恢复最近暂存 |
| `list` | 列出暂存 |
| `-u` | 包含未跟踪文件 |
| `--keep-index` | 保留已暂存区内容 |

## 示例

### 示例 1: 暂存并添加描述

```bash
git stash push -m "WIP: login feature"
```

### 示例 2: 恢复最近暂存并删除记录

```bash
git stash pop
```

### 示例 3: 列出所有暂存

```bash
git stash list
```

### 示例 4: 包含未跟踪文件一起暂存

```bash
git stash push -u
```

## 关联命令

- [[git-worktree|git worktree]]
- [[git-branch|git branch]]

## 风险提示

> ⚠️ **MEDIUM**: stash drop/clear 删除暂存不可恢复

## 最佳实践

[[bp-git-stash|git stash 生产环境最佳实践]]

## 所属维度

[[Git高级操作-MOC|版本控制/Git高级操作]]
