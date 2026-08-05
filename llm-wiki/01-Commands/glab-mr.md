---
{
  "cmd_name": "glab mr",
  "cmd_category": "CI-CD/平台工具",
  "cmd_dimension": "平台工具",
  "cmd_install": "同 glab",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "glab ci",
    "gh pr"
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

# glab mr

> 管理 GitLab Merge Request

## 安装

```bash
同 glab
```

## 用法

```
glab mr [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--source-branch` | 源分支 |
| `--target-branch` | 目标分支 |
| `--squash` | 合并时 squash commits |
| `--remove-source-branch` | 合并后删除源分支 |

## 示例

### 示例 1: 列出分配给我的 MR

```bash
glab mr list --assignee=@me
```

### 示例 2: 自动填充标题和描述创建 MR

```bash
glab mr create --fill
```

### 示例 3: Squash 合并 MR

```bash
glab mr merge 42 --squash --remove-source-branch
```

### 示例 4: 批准 MR

```bash
glab mr approve 42
```

## 关联命令

- [[glab-ci|glab ci]]
- [[gh-pr|gh pr]]

## 风险提示

> ⚠️ **MEDIUM**: merge 操作不可逆，确认代码已审查

## 最佳实践

[[bp-glab-mr|glab mr 生产环境最佳实践]]

## 所属维度

[[平台工具-MOC|CI-CD/平台工具]]
