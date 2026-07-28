---
{
  "cmd_name": "gh release",
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
    "goreleaser"
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

# gh release

> GitHub CLI Release 发布管理

## 安装

```bash
同 gh
```

## 用法

```
gh release [命令] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `create` | 创建 Release |
| `list` | 列出 Release |
| `upload` | 上传资产 |
| `--generate-notes` | 自动生成 changelog |

## 示例

### 示例 1: 创建 Release 并自动生成说明

```bash
gh release create v1.9.0 --generate-notes
```

### 示例 2: 创建 Release 并上传资产

```bash
gh release create v1.9.0 ./dist/*.tar.gz --title "v1.9.0"
```

### 示例 3: 列出最近 5 个 Release

```bash
gh release list --limit 5
```

### 示例 4: 下载指定版本资产

```bash
gh release download v1.8.0
```

## 关联命令

- [[gh-pr|gh pr]]
- [[goreleaser|goreleaser]]

## 风险提示

> ⚠️ **MEDIUM**: 发布后删除 Release 影响已分发的链接

## 所属维度

[[Git高级操作-MOC|版本控制/Git高级操作]]
