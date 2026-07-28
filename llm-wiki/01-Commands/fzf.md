---
{
  "cmd_name": "fzf",
  "cmd_category": "Shell脚本/现代工具",
  "cmd_dimension": "现代工具",
  "cmd_install": "brew install fzf (macOS) 或 apt install fzf (Ubuntu)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "rg",
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

# fzf

> 命令行模糊搜索工具，交互式过滤

## 安装

```bash
brew install fzf (macOS) 或 apt install fzf (Ubuntu)
```

## 用法

```
fzf [选项]
```

```
命令 | fzf [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--preview` | 预览窗口命令 |
| `--height` | 高度（不全屏） |
| `--multi` | 多选模式 |
| `--exact` | 精确匹配 |
| `--bind` | 绑定快捷键 |

## 示例

### 示例 1: 交互式模糊搜索当前目录文件

```bash
fzf
```

### 示例 2: 模糊搜索命令历史

```bash
history | fzf
```

### 示例 3: 搜索文件并预览内容

```bash
fzf --preview 'cat {}'
```

### 示例 4: 模糊搜索 Git 提交（多选）

```bash
git log --oneline | fzf --multi
```

## 关联命令

- [[rg|rg]]
- [[fd|fd]]

## 风险提示

> ⚠️ **LOW**: 只读/信息查询类命令，风险较低，但仍需确认目标对象。

## 所属维度

[[现代工具-MOC|Shell脚本/现代工具]]
