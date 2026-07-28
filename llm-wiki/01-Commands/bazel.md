---
{
  "cmd_name": "bazel",
  "cmd_category": "构建工具/CMake",
  "cmd_dimension": "CMake",
  "cmd_install": "brew install bazelisk (macOS) 或 apt install bazel-bootstrap (Ubuntu)",
  "cmd_platforms": [
    "linux",
    "darwin"
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

# bazel

> Google 开源的高性能多语言构建和测试工具

## 安装

```bash
brew install bazelisk (macOS) 或 apt install bazel-bootstrap (Ubuntu)
```

## 用法

```
bazel [命令] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `build` | 构建目标 |
| `test` | 运行测试 |
| `run` | 构建并运行 |
| `query` | 查询依赖图 |
| `--jobs` | 并行任务数 |

## 示例

### 示例 1: 构建指定目标

```bash
bazel build //src/main:app
```

### 示例 2: 运行所有测试（仅显示失败）

```bash
bazel test //src/... --test_output=errors
```

### 示例 3: 查询依赖图

```bash
bazel query "deps(//src/main:app)" --output graph
```

### 示例 4: 构建并运行服务

```bash
bazel run //tools:server
```

## 关联命令

- [[cmake|cmake]]
- [[make|make]]

## 风险提示

> ⚠️ **LOW**: 构建和测试操作风险低

## 所属维度

[[CMake-MOC|构建工具/CMake]]
