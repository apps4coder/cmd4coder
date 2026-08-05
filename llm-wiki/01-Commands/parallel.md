---
{
  "cmd_name": "parallel",
  "cmd_category": "Shell脚本/文本处理",
  "cmd_dimension": "文本处理",
  "cmd_install": "brew install parallel (macOS) 或 apt install parallel (Ubuntu)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "xargs",
    "find"
  ],
  "cmd_tags": [
    "distributed",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/shell/text-processing.yaml"
}
---

# parallel

> GNU Parallel 并行命令执行工具

## 安装

```bash
brew install parallel (macOS) 或 apt install parallel (Ubuntu)
```

## 用法

```
parallel [选项] [命令] ::: [参数]
```

```
命令 | parallel [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `-j` | 并行任务数（默认 CPU 核数） |
| `--bar` | 显示进度条 |
| `--dry-run` | 仅打印将执行的命令 |
| `-X` | 多参数模式 |

## 示例

### 示例 1: 4 路并行转换 JPG 为 PNG

```bash
parallel -j 4 convert {} {.}.png ::: *.jpg
```

### 示例 2: 10 路并行检查服务器状态

```bash
cat servers.txt | parallel -j 10 ssh {} uptime
```

### 示例 3: 带进度条并行压缩日志

```bash
parallel --bar gzip ::: *.log
```

### 示例 4: 预览将执行的命令

```bash
parallel --dry-run echo {} ::: a b c
```

## 关联命令

- [[xargs|xargs]]
- [[find|find]]

## 风险提示

> ⚠️ **HIGH**: 并行执行放大操作影响，--dry-run 先预览

## 最佳实践

[[bp-parallel|parallel 生产环境最佳实践]]

## 所属维度

[[文本处理-MOC|Shell脚本/文本处理]]
