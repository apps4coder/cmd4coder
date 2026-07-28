---
{
  "cmd_name": "ruff",
  "cmd_category": "编程语言/Python工具链扩展",
  "cmd_dimension": "Python工具链扩展",
  "cmd_install": "pip install ruff 或 brew install ruff (macOS)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "black",
    "mypy"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/lang/python-tooling.yaml"
}
---

# ruff

> 极速 Python linter 和 formatter（替代 flake8+isort+black）

## 安装

```bash
pip install ruff 或 brew install ruff (macOS)
```

## 用法

```
ruff [命令] [选项] [路径]
```

## 参数

| Flag | Description |
|------|-------------|
| `check` | 运行 lint 检查 |
| `format` | 格式化代码 |
| `--fix` | 自动修复 |
| `--select` | 选择规则集 |
| `--ignore` | 忽略规则 |

## 示例

### 示例 1: 检查当前目录所有 Python 文件

```bash
ruff check .
```

### 示例 2: 自动修复可修复的问题

```bash
ruff check --fix .
```

### 示例 3: 格式化所有 Python 文件

```bash
ruff format .
```

### 示例 4: 仅检查 pycodestyle+pyflakes+isort 规则

```bash
ruff check --select E,F,I .
```

## 关联命令

- [[black|black]]
- [[mypy|mypy]]

## 风险提示

> ⚠️ **LOW**: --fix 和 format 修改文件，建议配合 Git 使用

## 所属维度

[[Python工具链扩展-MOC|编程语言/Python工具链扩展]]
