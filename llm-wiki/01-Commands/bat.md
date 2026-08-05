---
{
  "cmd_name": "bat",
  "cmd_category": "Shell脚本/现代工具",
  "cmd_dimension": "现代工具",
  "cmd_install": "brew install bat (macOS) 或 apt install bat (Ubuntu，命令为 batcat)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cat",
    "delta"
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

# bat

> 带语法高亮和 Git 集成的 cat 替代品

## 安装

```bash
brew install bat (macOS) 或 apt install bat (Ubuntu，命令为 batcat)
```

## 用法

```
bat [选项] [文件]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 仅显示行号（无网格） |
| `-p` | 纯输出（无装饰，类似 cat） |
| `-l` | 指定语言高亮 |
| `-r` | 显示指定行范围 |
| `--diff` | 显示 Git 变更标记 |

## 示例

### 示例 1: 语法高亮查看 Go 文件

```bash
bat main.go
```

### 示例 2: 查看第 100-150 行

```bash
bat -n -r 100:150 file.py
```

### 示例 3: 查看文件并标记 Git 变更

```bash
bat --diff src/main.rs
```

### 示例 4: 纯文本输出（管道友好）

```bash
bat -p file.txt
```

## 关联命令

- [[cat|cat]]
- [[delta|delta]]

## 风险提示

> ⚠️ **LOW**: 只读操作，无风险

## 最佳实践

[[bp-bat|bat 生产环境最佳实践]]

## 所属维度

[[现代工具-MOC|Shell脚本/现代工具]]
