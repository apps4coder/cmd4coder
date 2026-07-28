---
{
  "cmd_name": "git submodule",
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
    "git clone",
    "git worktree"
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

# git submodule

> Git 子模块管理（嵌套仓库依赖）

## 用法

```
git submodule [命令] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `add` | 添加子模块 |
| `update` | 更新子模块 |
| `init` | 初始化子模块 |
| `foreach` | 对每个子模块执行命令 |
| `--recursive` | 递归处理嵌套子模块 |

## 示例

### 示例 1: 添加子模块

```bash
git submodule add https://github.com/lib/dep.git vendor/dep
```

### 示例 2: 初始化并更新所有子模块

```bash
git submodule update --init --recursive
```

### 示例 3: 所有子模块拉取最新

```bash
git submodule foreach git pull origin main
```

### 示例 4: 查看子模块状态

```bash
git submodule status
```

## 关联命令

- [[git-clone|git clone]]
- [[git-worktree|git worktree]]

## 风险提示

> ⚠️ **MEDIUM**: 子模块版本锁定，更新不当导致依赖不一致

## 所属维度

[[Git高级操作-MOC|版本控制/Git高级操作]]
