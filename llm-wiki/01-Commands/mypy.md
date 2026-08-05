---
{
  "cmd_name": "mypy",
  "cmd_category": "编程语言/Python工具链扩展",
  "cmd_dimension": "Python工具链扩展",
  "cmd_install": "pip install mypy 或 brew install mypy (macOS)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ruff",
    "pytest"
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

# mypy

> Python 静态类型检查器

## 安装

```bash
pip install mypy 或 brew install mypy (macOS)
```

## 用法

```
mypy [选项] [路径]
```

## 参数

| Flag | Description |
|------|-------------|
| `--strict` | 严格模式（所有检查开启） |
| `--ignore-missing-imports` | 忽略缺失的第三方类型 |
| `--show-error-codes` | 显示错误代码 |
| `--python-version` | 目标 Python 版本 |

## 示例

### 示例 1: 检查 src 目录类型

```bash
mypy src/
```

### 示例 2: 严格模式检查

```bash
mypy --strict src/
```

### 示例 3: 忽略第三方库类型缺失

```bash
mypy --ignore-missing-imports .
```

### 示例 4: 指定版本检查

```bash
mypy --show-error-codes --python-version 3.12 src/
```

## 关联命令

- [[ruff|ruff]]
- [[pytest|pytest]]

## 风险提示

> ⚠️ **LOW**: 只读检查操作，无风险

## 最佳实践

[[bp-mypy|mypy 生产环境最佳实践]]

## 所属维度

[[Python工具链扩展-MOC|编程语言/Python工具链扩展]]
