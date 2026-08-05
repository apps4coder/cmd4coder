---
{
  "cmd_name": "svn revert",
  "cmd_category": "Version Control",
  "cmd_dimension": "Version Control",
  "cmd_install": "Install Subversion package",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/vcs/svn.yaml"
}
---

# svn revert

> Undo local changes

## 安装

```bash
Install Subversion package
```

## 用法

```
svn revert PATH
```

## 参数

| Flag | Description |
|------|-------------|
| `-R` | Recursive revert |

## 示例

### 示例 1: Revert changes to file

```bash
svn revert file.txt
```

### 示例 2: Revert all changes recursively

```bash
svn revert -R .
```

## 风险提示

> ⚠️ **HIGH**: Permanently discards uncommitted changes; cannot be undone

> ⚠️ **HIGH**: 涉及删除或回退的操作不可逆，建议先备份工作副本或确认提交范围。

## 最佳实践

[[bp-svn-revert|svn revert 生产环境最佳实践]]

## 所属维度

[[Version Control-MOC|Version Control]]
