---
{
  "cmd_name": "svn merge",
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

# svn merge

> Merge changes from another branch

## 安装

```bash
Install Subversion package
```

## 用法

```
svn merge SOURCE[@REV] [TARGET]
```

## 示例

### 示例 1: Merge feature branch to current branch

```bash
svn merge ^/branches/feature
```

### 示例 2: Merge specific revisions

```bash
svn merge -r 1234:1240 ^/trunk
```

## 风险提示

> ⚠️ **HIGH**: May cause conflicts; review changes before committing

> ⚠️ **HIGH**: 涉及删除或回退的操作不可逆，建议先备份工作副本或确认提交范围。

## 最佳实践

[[bp-svn-merge|svn merge 生产环境最佳实践]]

## 所属维度

[[Version Control-MOC|Version Control]]
