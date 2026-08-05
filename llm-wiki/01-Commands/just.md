---
{
  "cmd_name": "just",
  "cmd_category": "构建工具/CMake",
  "cmd_dimension": "CMake",
  "cmd_install": "brew install just (macOS) 或 cargo install just",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "make",
    "task"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/build-tools/cmake.yaml"
}
---

# just

> 现代命令运行器（Makefile 的简洁替代）

## 安装

```bash
brew install just (macOS) 或 cargo install just
```

## 用法

```
just [选项] [recipe]
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | 列出所有 recipe |
| `-f` | 指定 justfile 路径 |
| `--show` | 显示 recipe 内容 |
| `--dry-run` | 仅打印将执行的命令 |

## 示例

### 示例 1: 运行默认 recipe

```bash
just
```

### 示例 2: 列出所有可用命令

```bash
just -l
```

### 示例 3: 运行 build recipe 传入参数

```bash
just build release
```

### 示例 4: 查看 test recipe 定义

```bash
just --show test
```

## 关联命令

- [[make|make]]

## 风险提示

> ⚠️ **MEDIUM**: recipe 可执行任意命令，审查 justfile 内容

## 最佳实践

[[bp-just|just 生产环境最佳实践]]

## 所属维度

[[CMake-MOC|构建工具/CMake]]
