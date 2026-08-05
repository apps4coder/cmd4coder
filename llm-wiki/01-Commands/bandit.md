---
{
  "cmd_name": "bandit",
  "cmd_category": "编程语言/Python工具链扩展",
  "cmd_dimension": "Python工具链扩展",
  "cmd_install": "pip install bandit",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ruff",
    "safety"
  ],
  "cmd_tags": [
    "safety",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/lang/python-tooling.yaml"
}
---

# bandit

> Python 安全漏洞扫描工具

## 安装

```bash
pip install bandit
```

## 用法

```
bandit [选项] [路径]
```

## 参数

| Flag | Description |
|------|-------------|
| `-r` | 递归扫描 |
| `-ll` | 仅显示中高危 |
| `-f` | 输出格式 (json/csv/html) |
| `--skip` | 跳过检查项 |

## 示例

### 示例 1: 递归扫描安全问题

```bash
bandit -r src/
```

### 示例 2: 仅显示中高危问题

```bash
bandit -r -ll src/
```

### 示例 3: JSON 格式输出报告

```bash
bandit -r -f json -o report.json src/
```

### 示例 4: 跳过 assert 检查

```bash
bandit -r --skip B101 src/
```

## 关联命令

- [[ruff|ruff]]

## 风险提示

> ⚠️ **LOW**: 只读扫描操作，无风险

## 最佳实践

[[bp-bandit|bandit 生产环境最佳实践]]

## 所属维度

[[Python工具链扩展-MOC|编程语言/Python工具链扩展]]
