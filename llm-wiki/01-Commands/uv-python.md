---
{
  "cmd_name": "uv python",
  "cmd_category": "构建工具/包管理",
  "cmd_dimension": "包管理",
  "cmd_install": "同 uv",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "uv",
    "pyenv"
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

# uv python

> 管理 Python 解释器版本

## 安装

```bash
同 uv
```

## 用法

```
uv python [命令] [版本]
```

## 参数

| Flag | Description |
|------|-------------|
| `install` | 安装指定版本 |
| `list` | 列出可用版本 |
| `pin` | 固定项目 Python 版本 |

## 示例

### 示例 1: 安装 Python 3.12

```bash
uv python install 3.12
```

### 示例 2: 列出已安装和可用版本

```bash
uv python list
```

### 示例 3: 固定项目使用 Python 3.12

```bash
uv python pin 3.12
```

### 示例 4: 查找当前使用的 Python 路径

```bash
uv python find
```

## 关联命令

- [[uv|uv]]

## 风险提示

> ⚠️ **LOW**: 仅管理本地 Python 版本

## 最佳实践

[[bp-uv-python|uv python 生产环境最佳实践]]

## 所属维度

[[包管理-MOC|构建工具/包管理]]
