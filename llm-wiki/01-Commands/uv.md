---
{
  "cmd_name": "uv",
  "cmd_category": "构建工具/包管理",
  "cmd_dimension": "包管理",
  "cmd_install": "curl -LsSf https://astral.sh/uv/install.sh | sh 或 brew install uv (macOS)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "pip",
    "poetry"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/build-tools/pkg-mgmt.yaml"
}
---

# uv

> 极速 Python 包管理器和项目管理工具（pip/venv 的现代替代）

## 安装

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh 或 brew install uv (macOS)
```

## 用法

```
uv [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--python` | 指定 Python 版本 |
| `--upgrade` | 升级到最新版本 |
| `-q` | 静默模式 |

## 示例

### 示例 1: 创建虚拟环境

```bash
uv venv
```

### 示例 2: 极速安装包（比 pip 快 10-100x）

```bash
uv pip install requests flask
```

### 示例 3: 初始化新项目

```bash
uv init my-project
```

### 示例 4: 在项目环境中运行命令

```bash
uv run pytest
```

## 关联命令

- [[pip|pip]]
- [[poetry|poetry]]

## 风险提示

> ⚠️ **LOW**: 包管理操作风险低

## 所属维度

[[包管理-MOC|构建工具/包管理]]
