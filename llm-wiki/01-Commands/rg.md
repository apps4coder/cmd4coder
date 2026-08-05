---
{
  "cmd_name": "rg",
  "cmd_category": "Shell脚本/现代工具",
  "cmd_dimension": "现代工具",
  "cmd_install": "brew install ripgrep (macOS) 或 apt install ripgrep (Ubuntu)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "grep",
    "fd"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/shell/modern-tools.yaml"
}
---

# rg

> ripgrep 极速文本搜索工具（grep 的现代替代）

## 安装

```bash
brew install ripgrep (macOS) 或 apt install ripgrep (Ubuntu)
```

## 用法

```
rg [选项] [模式] [路径]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 忽略大小写 |
| `-t` | 按文件类型过滤 (-t go/-t py) |
| `-l` | 仅输出文件名 |
| `-c` | 输出匹配计数 |
| `-A / -B / -C` | 上下文行数 |
| `--hidden` | 搜索隐藏文件 |
| `-g` | glob 过滤 (-g "*.yaml") |

## 示例

### 示例 1: 在 Go 文件中搜索 TODO

```bash
rg "TODO" -t go
```

### 示例 2: 忽略大小写搜索，显示 3 行上下文

```bash
rg -i "error" -C 3
```

### 示例 3: 列出包含 import 的 Python 文件

```bash
rg -l "import" -g "*.py"
```

### 示例 4: 搜索隐藏文件但排除 .git

```bash
rg --hidden -g "!.git" "config"
```

## 关联命令

- [[grep|grep]]
- [[fd|fd]]

## 风险提示

> ⚠️ **LOW**: 只读/信息查询类命令，风险较低，但仍需确认目标对象。

## 最佳实践

[[bp-rg|rg 生产环境最佳实践]]

## 所属维度

[[现代工具-MOC|Shell脚本/现代工具]]
