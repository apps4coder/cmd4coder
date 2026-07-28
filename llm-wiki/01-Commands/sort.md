---
{
  "cmd_name": "sort",
  "cmd_category": "Shell脚本/文本处理",
  "cmd_dimension": "文本处理",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "uniq",
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

# sort

> 文本排序工具

## 用法

```
sort [选项] [文件]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 数值排序 |
| `-r` | 逆序 |
| `-u` | 去重 |
| `-k` | 按指定列排序 |
| `-t` | 指定分隔符 |
| `-h` | 人类可读大小排序 (1K/2M/3G) |

## 示例

### 示例 1: 数值排序

```bash
sort -n numbers.txt
```

### 示例 2: 按 UID（第 3 列）数值排序

```bash
sort -t: -k3 -n /etc/passwd
```

### 示例 3: 按文件大小降序排列

```bash
du -sh * | sort -hr
```

### 示例 4: 排序并去重

```bash
sort -u file.txt
```

## 关联命令

- [[uniq|uniq]]
- [[awk|awk]]

## 风险提示

> ⚠️ **LOW**: 只读操作，无风险

## 所属维度

[[文本处理-MOC|Shell脚本/文本处理]]
