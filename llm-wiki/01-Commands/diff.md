---
{
  "cmd_name": "diff",
  "cmd_category": "Shell脚本/文本处理",
  "cmd_dimension": "文本处理",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "git diff",
    "colordiff"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/shell/text-processing.yaml"
}
---

# diff

> 逐行比较文件差异

## 用法

```
diff [选项] 文件1 文件2
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | 统一格式（unified diff） |
| `-r` | 递归比较目录 |
| `-w` | 忽略空白差异 |
| `-y` | 并排显示 |
| `--color` | 彩色输出 |

## 示例

### 示例 1: 统一格式比较配置变更

```bash
diff -u old.conf new.conf
```

### 示例 2: 递归比较两个目录

```bash
diff -r src/ src-backup/
```

### 示例 3: 并排彩色对比

```bash
diff -y --color file1 file2
```

### 示例 4: 比较排序后的内容差异

```bash
diff <(sort file1) <(sort file2)
```

## 关联命令

- [[git-diff|git diff]]

## 风险提示

> ⚠️ **LOW**: 只读操作，无风险

## 所属维度

[[文本处理-MOC|Shell脚本/文本处理]]
