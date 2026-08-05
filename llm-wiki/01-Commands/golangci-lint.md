---
{
  "cmd_name": "golangci-lint",
  "cmd_category": "编程语言/Go工具链扩展",
  "cmd_dimension": "Go工具链扩展",
  "cmd_install": "brew install golangci-lint (macOS) 或 curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "staticcheck",
    "go vet"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/lang/go-tooling.yaml"
}
---

# golangci-lint

> Go 代码 lint 聚合工具（集成 50+ linter）

## 安装

```bash
brew install golangci-lint (macOS) 或 curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh
```

## 用法

```
golangci-lint [命令] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行检查 |
| `--enable` | 启用 linter |
| `--disable` | 禁用 linter |
| `--fix` | 自动修复 |
| `-v` | 详细输出 |

## 示例

### 示例 1: 运行所有已启用 linter

```bash
golangci-lint run
```

### 示例 2: 自动修复可修复的问题

```bash
golangci-lint run --fix
```

### 示例 3: 启用额外 linter

```bash
golangci-lint run --enable gosec,bodyclose
```

### 示例 4: 检查指定包

```bash
golangci-lint run ./cmd/... ./internal/...
```

## 关联命令

- [[staticcheck|staticcheck]]
- [[go-vet|go vet]]

## 风险提示

> ⚠️ **LOW**: --fix 修改文件，建议配合 Git 使用

## 最佳实践

[[bp-golangci-lint|golangci-lint 生产环境最佳实践]]

## 所属维度

[[Go工具链扩展-MOC|编程语言/Go工具链扩展]]
