---
{
  "cmd_name": "black",
  "cmd_category": "编程语言/Python工具链扩展",
  "cmd_dimension": "Python工具链扩展",
  "cmd_install": "pip install black 或 brew install black (macOS)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ruff",
    "isort"
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

# black

> Python 代码格式化工具（无争议风格）

## 安装

```bash
pip install black 或 brew install black (macOS)
```

## 用法

```
black [选项] [路径]
```

## 参数

| Flag | Description |
|------|-------------|
| `--check` | 仅检查不修改 |
| `--diff` | 显示差异 |
| `-l` | 行宽限制（默认 88） |
| `--target-version` | 目标 Python 版本 |

## 示例

### 示例 1: 格式化当前目录

```bash
black .
```

### 示例 2: 检查格式差异（CI 用）

```bash
black --check --diff src/
```

### 示例 3: 120 字符行宽格式化

```bash
black -l 120 src/
```

### 示例 4: 针对 Python 3.12 格式化

```bash
black --target-version py312 .
```

## 关联命令

- [[ruff|ruff]]

## 风险提示

> ⚠️ **LOW**: 修改文件格式，建议配合 Git 使用

## 所属维度

[[Python工具链扩展-MOC|编程语言/Python工具链扩展]]
