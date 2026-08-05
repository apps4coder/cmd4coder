---
{
  "cmd_name": "fd",
  "cmd_category": "Shell脚本/现代工具",
  "cmd_dimension": "现代工具",
  "cmd_install": "brew install fd (macOS) 或 apt install fd-find (Ubuntu，命令为 fdfind)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "find",
    "rg"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/shell/modern-tools.yaml"
}
---

# fd

> 快速文件查找工具（find 的现代替代）

## 安装

```bash
brew install fd (macOS) 或 apt install fd-find (Ubuntu，命令为 fdfind)
```

## 用法

```
fd [选项] [模式] [路径]
```

## 参数

| Flag | Description |
|------|-------------|
| `-e` | 按扩展名过滤 (-e go/-e yaml) |
| `-t` | 按类型 (f=文件/d=目录/l=链接) |
| `-H` | 包含隐藏文件 |
| `-I` | 不遵循 .gitignore |
| `-x` | 对结果执行命令 |
| `-p` | 匹配完整路径 |

## 示例

### 示例 1: 查找所有 Go 文件

```bash
fd -e go
```

### 示例 2: 查找名为 node_modules 的目录

```bash
fd -t d node_modules
```

### 示例 3: 查找所有 .env 文件（含隐藏、忽略 gitignore）

```bash
fd -H -I ".env"
```

### 示例 4: 查找并删除所有 .log 文件

```bash
fd -e log -x rm {}
```

## 关联命令

- [[find|find]]
- [[rg|rg]]

## 风险提示

> ⚠️ **HIGH**: -x 配合 rm 等命令可批量删除文件

## 最佳实践

[[bp-fd|fd 生产环境最佳实践]]

## 所属维度

[[现代工具-MOC|Shell脚本/现代工具]]
