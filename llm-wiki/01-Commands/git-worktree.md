---
{
  "cmd_name": "git worktree",
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
    "git branch",
    "git checkout"
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

# git worktree

> 多工作树管理（同时检出多个分支到不同目录）

## 用法

```
git worktree [命令] [路径] [分支]
```

## 参数

| Flag | Description |
|------|-------------|
| `add` | 添加工作树 |
| `list` | 列出工作树 |
| `remove` | 删除工作树 |
| `prune` | 清理无效工作树 |

## 示例

### 示例 1: 在 ../hotfix 目录检出热修复分支

```bash
git worktree add ../hotfix hotfix/v1.2.1
```

### 示例 2: 列出所有工作树

```bash
git worktree list
```

### 示例 3: 删除工作树

```bash
git worktree remove ../hotfix
```

### 示例 4: 基于 main 创建新分支并检出到工作树

```bash
git worktree add -b feature/new ../feature-new main
```

## 关联命令

- [[git-branch|git branch]]
- [[git-checkout|git checkout]]

## 风险提示

> ⚠️ **LOW**: 工作树操作风险低，remove 前确认无未提交变更

## 所属维度

[[Git高级操作-MOC|版本控制/Git高级操作]]
