---
{
  "cmd_name": "eza",
  "cmd_category": "Shell脚本/现代工具",
  "cmd_dimension": "现代工具",
  "cmd_install": "brew install eza (macOS) 或 cargo install eza",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ls",
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

# eza

> 现代 ls 替代品（彩色、图标、Git 状态）

## 安装

```bash
brew install eza (macOS) 或 cargo install eza
```

## 用法

```
eza [选项] [路径]
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | 长格式列表 |
| `-a` | 显示隐藏文件 |
| `--tree` | 树形显示 |
| `--git` | 显示 Git 状态 |
| `--icons` | 显示文件图标 |
| `-s` | 排序字段 (name/size/date) |

## 示例

### 示例 1: 长格式+Git 状态+图标

```bash
eza -la --git --icons
```

### 示例 2: 两层目录树

```bash
eza --tree --level=2
```

### 示例 3: 按大小排序

```bash
eza -l -s size
```

### 示例 4: 隐藏 .gitignore 中的文件

```bash
eza -la --git-ignore
```

## 关联命令

- [[ls|ls]]
- [[fd|fd]]

## 风险提示

> ⚠️ **LOW**: 只读操作，无风险

## 最佳实践

[[bp-eza|eza 生产环境最佳实践]]

## 所属维度

[[现代工具-MOC|Shell脚本/现代工具]]
