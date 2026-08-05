---
{
  "cmd_name": "ninja",
  "cmd_category": "构建工具/CMake",
  "cmd_dimension": "CMake",
  "cmd_install": "brew install ninja (macOS) 或 apt install ninja-build (Ubuntu)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cmake",
    "make"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/build-tools/cmake.yaml"
}
---

# ninja

> 小型快速构建系统，通常由 CMake 生成

## 安装

```bash
brew install ninja (macOS) 或 apt install ninja-build (Ubuntu)
```

## 用法

```
ninja [选项] [目标]
```

## 参数

| Flag | Description |
|------|-------------|
| `-C` | 指定构建目录 |
| `-j` | 并行任务数 |
| `-t` | 工具模式 (targets/clean/commands) |
| `-v` | 显示完整命令 |

## 示例

### 示例 1: 在 build 目录构建

```bash
ninja -C build
```

### 示例 2: 8 路并行构建

```bash
ninja -C build -j 8
```

### 示例 3: 清理构建产物

```bash
ninja -C build -t clean
```

### 示例 4: 列出所有可用目标

```bash
ninja -C build -t targets all
```

## 关联命令

- [[cmake|cmake]]
- [[make|make]]

## 风险提示

> ⚠️ **LOW**: 构建操作风险低

## 最佳实践

[[bp-ninja|ninja 生产环境最佳实践]]

## 所属维度

[[CMake-MOC|构建工具/CMake]]
