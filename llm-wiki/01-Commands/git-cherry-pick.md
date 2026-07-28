---
{
  "cmd_name": "git cherry-pick",
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
    "git rebase",
    "git merge"
  ],
  "cmd_tags": [
    "application",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/vcs/git-advanced.yaml"
}
---

# git cherry-pick

> 选择性应用指定提交到当前分支

## 用法

```
git cherry-pick [选项] [提交]
```

## 参数

| Flag | Description |
|------|-------------|
| `-x` | 在提交信息中追加来源 |
| `--no-commit` | 仅应用变更不提交 |
| `-n` | 同 --no-commit |
| `--abort` | 中止操作 |

## 示例

### 示例 1: 应用指定提交

```bash
git cherry-pick abc1234
```

### 示例 2: 应用并标注来源

```bash
git cherry-pick -x abc1234
```

### 示例 3: 合并多个提交变更但不提交

```bash
git cherry-pick --no-commit abc1234 def5678
```

### 示例 4: 中止冲突的 cherry-pick

```bash
git cherry-pick --abort
```

## 关联命令

- [[git-rebase|git rebase]]
- [[git-merge|git merge]]

## 风险提示

> ⚠️ **MEDIUM**: 可能产生冲突，重复 cherry-pick 导致重复变更

## 所属维度

[[Git高级操作-MOC|版本控制/Git高级操作]]
