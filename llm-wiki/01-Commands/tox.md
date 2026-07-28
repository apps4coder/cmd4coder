---
{
  "cmd_name": "tox",
  "cmd_category": "编程语言/Python工具链扩展",
  "cmd_dimension": "Python工具链扩展",
  "cmd_install": "pip install tox",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "pytest",
    "nox"
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

# tox

> Python 多环境测试自动化工具

## 安装

```bash
pip install tox
```

## 用法

```
tox [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `-e` | 指定环境 |
| `-p` | 并行执行 |
| `--listenvs` | 列出所有环境 |

## 示例

### 示例 1: 运行所有测试环境

```bash
tox
```

### 示例 2: 仅运行 Python 3.12 环境

```bash
tox -e py312
```

### 示例 3: 运行 lint 环境

```bash
tox -e lint
```

### 示例 4: 并行运行所有环境

```bash
tox -p auto
```

## 关联命令

- [[pytest|pytest]]

## 风险提示

> ⚠️ **LOW**: 测试执行操作，无风险

## 所属维度

[[Python工具链扩展-MOC|编程语言/Python工具链扩展]]
