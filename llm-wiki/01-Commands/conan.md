---
{
  "cmd_name": "conan",
  "cmd_category": "构建工具/CMake",
  "cmd_dimension": "CMake",
  "cmd_install": "pip install conan 或 brew install conan (macOS)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cmake",
    "vcpkg"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/build-tools/cmake.yaml"
}
---

# conan

> C/C++ 包管理器

## 安装

```bash
pip install conan 或 brew install conan (macOS)
```

## 用法

```
conan [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `install` | 安装依赖 |
| `create` | 创建包 |
| `search` | 搜索远程包 |

## 示例

### 示例 1: 安装依赖（缺失时从源码构建）

```bash
conan install . --output-folder=build --build=missing
```

### 示例 2: 创建并导出包

```bash
conan create . --version=1.0.0
```

### 示例 3: 在远程仓库搜索包

```bash
conan search "fmt/*" -r conancenter
```

### 示例 4: 自动检测编译器配置

```bash
conan profile detect
```

## 关联命令

- [[cmake|cmake]]

## 风险提示

> ⚠️ **LOW**: 包管理操作风险低

## 所属维度

[[CMake-MOC|构建工具/CMake]]
