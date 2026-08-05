---
{
  "cmd_name": "mise",
  "cmd_category": "Shell脚本/现代工具",
  "cmd_dimension": "现代工具",
  "cmd_install": "brew install mise (macOS) 或 curl https://mise.run | sh",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "nvm",
    "pyenv"
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

# mise

> 多语言运行时版本管理器（asdf 的现代替代）

## 安装

```bash
brew install mise (macOS) 或 curl https://mise.run | sh
```

## 用法

```
mise [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `install` | 安装指定版本 |
| `use` | 设置当前目录使用的版本 |
| `ls` | 列出已安装版本 |
| `exec` | 在指定版本环境中执行命令 |

## 示例

### 示例 1: 设置当前项目使用 Node 20 和 Python 3.12

```bash
mise use node@20 python@3.12
```

### 示例 2: 安装 .mise.toml 中定义的所有工具

```bash
mise install
```

### 示例 3: 列出已安装的工具和版本

```bash
mise ls
```

### 示例 4: 在项目环境中执行命令

```bash
mise exec -- node --version
```

## 风险提示

> ⚠️ **LOW**: 仅管理本地运行时版本，无风险

## 最佳实践

[[bp-mise|mise 生产环境最佳实践]]

## 所属维度

[[现代工具-MOC|Shell脚本/现代工具]]
