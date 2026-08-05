---
{
  "cmd_name": "poetry",
  "cmd_category": "构建工具/包管理",
  "cmd_dimension": "包管理",
  "cmd_install": "curl -sSL https://install.python-poetry.org | python3 - 或 brew install poetry (macOS)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "uv",
    "pip"
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

# poetry

> Python 项目依赖管理和打包工具

## 安装

```bash
curl -sSL https://install.python-poetry.org | python3 - 或 brew install poetry (macOS)
```

## 用法

```
poetry [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--no-interaction` | 非交互模式 |
| `-v` | 详细输出 |

## 示例

### 示例 1: 交互式初始化项目

```bash
poetry init
```

### 示例 2: 添加依赖

```bash
poetry add requests numpy
```

### 示例 3: 添加开发依赖

```bash
poetry add --group dev pytest ruff
```

### 示例 4: 安装所有依赖

```bash
poetry install
```

### 示例 5: 在虚拟环境中运行

```bash
poetry run python main.py
```

### 示例 6: 构建分发包

```bash
poetry build
```

## 关联命令

- [[uv|uv]]
- [[pip|pip]]

## 风险提示

> ⚠️ **LOW**: 包管理操作风险低

## 最佳实践

[[bp-poetry|poetry 生产环境最佳实践]]

## 所属维度

[[包管理-MOC|构建工具/包管理]]
