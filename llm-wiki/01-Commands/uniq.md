---
{
  "cmd_name": "uniq",
  "cmd_category": "Shell脚本/文本处理",
  "cmd_dimension": "文本处理",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "sort",
    "awk"
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

# uniq

> 报告或过滤重复行（需先排序）

## 用法

```
uniq [选项] [文件]
```

```
sort file | uniq [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | 显示每行出现次数 |
| `-d` | 仅输出重复行 |
| `-u` | 仅输出唯一行 |
| `-i` | 忽略大小写 |

## 示例

### 示例 1: 统计访问频率 Top 10

```bash
sort access.log | uniq -c | sort -rn | head
```

### 示例 2: 找出重复行

```bash
sort file.txt | uniq -d
```

### 示例 3: 找出唯一行

```bash
sort file.txt | uniq -u
```

## 关联命令

- [[sort|sort]]
- [[awk|awk]]

## 风险提示

> ⚠️ **LOW**: 只读操作，无风险

## 所属维度

[[文本处理-MOC|Shell脚本/文本处理]]
