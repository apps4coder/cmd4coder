---
{
  "cmd_name": "ctest",
  "cmd_category": "构建工具/CMake",
  "cmd_dimension": "CMake",
  "cmd_install": "随 cmake 安装",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cmake",
    "make test"
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

# ctest

> CMake 测试驱动器

## 安装

```bash
随 cmake 安装
```

## 用法

```
ctest [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--test-dir` | 测试目录 |
| `-j` | 并行测试数 |
| `-R` | 正则过滤测试名 |
| `--output-on-failure` | 失败时显示输出 |
| `-V` | 详细输出 |

## 示例

### 示例 1: 运行所有测试

```bash
ctest --test-dir build
```

### 示例 2: 4 路并行，失败显示输出

```bash
ctest --test-dir build -j 4 --output-on-failure
```

### 示例 3: 仅运行 unit_ 开头的测试

```bash
ctest --test-dir build -R "unit_.*"
```

### 示例 4: 详细模式查看所有测试输出

```bash
ctest --test-dir build -V
```

## 关联命令

- [[cmake|cmake]]

## 风险提示

> ⚠️ **LOW**: 只读测试操作，无风险

## 所属维度

[[CMake-MOC|构建工具/CMake]]
