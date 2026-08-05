---
{
  "cmd_name": "cut",
  "cmd_category": "Shell脚本/文本处理",
  "cmd_dimension": "文本处理",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "awk",
    "sed"
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

# cut

> 按列切割文本行

## 用法

```
cut [选项] [文件]
```

## 参数

| Flag | Description |
|------|-------------|
| `-d` | 指定分隔符 |
| `-f` | 选择字段（列号） |
| `-c` | 选择字符位置 |

## 示例

### 示例 1: 提取用户名（第一列）

```bash
cut -d: -f1 /etc/passwd
```

### 示例 2: 提取第 1 和第 3 列

```bash
cut -d' ' -f1,3 data.txt
```

### 示例 3: 提取每行前 10 个字符

```bash
cut -c1-10 file.txt
```

## 关联命令

- [[awk|awk]]
- [[sed|sed]]

## 风险提示

> ⚠️ **LOW**: 只读操作，无风险

## 最佳实践

[[bp-cut|cut 生产环境最佳实践]]

## 所属维度

[[文本处理-MOC|Shell脚本/文本处理]]
