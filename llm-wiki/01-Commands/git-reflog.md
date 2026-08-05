---
{
  "cmd_name": "git reflog",
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
    "git reset",
    "git stash"
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

# git reflog

> 引用日志，恢复误操作（找回丢失的提交和分支）

## 用法

```
git reflog [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--all` | 显示所有引用 |
| `-n` | 限制显示条数 |
| `--date` | 显示日期格式 |

## 示例

### 示例 1: 查看 HEAD 移动历史

```bash
git reflog
```

### 示例 2: 查看最近 20 条记录

```bash
git reflog -n 20
```

### 示例 3: 从 reflog 恢复 3 步前的状态

```bash
git checkout -b recovered HEAD@{3}
```

### 示例 4: 恢复到上一步操作前的状态

```bash
git reset --hard HEAD@{1}
```

## 关联命令

- [[git-stash|git stash]]

## 风险提示

> ⚠️ **MEDIUM**: 配合 reset --hard 使用时会丢弃工作区变更

## 最佳实践

[[bp-git-reflog|git reflog 生产环境最佳实践]]

## 所属维度

[[Git高级操作-MOC|版本控制/Git高级操作]]
