---
{
  "cmd_name": "go generate",
  "cmd_category": "编程语言/Go工具链扩展",
  "cmd_dimension": "Go工具链扩展",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "go build",
    "mockgen"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/lang/go-tooling.yaml"
}
---

# go generate

> 执行 Go 代码生成指令（//go:generate 注释）

## 用法

```
go generate [选项] [包]
```

## 参数

| Flag | Description |
|------|-------------|
| `-v` | 显示执行的命令 |
| `-x` | 打印命令但不执行 |
| `-run` | 正则过滤生成指令 |

## 示例

### 示例 1: 递归执行所有代码生成

```bash
go generate ./...
```

### 示例 2: 详细模式生成指定包

```bash
go generate -v ./internal/model/
```

### 示例 3: 仅执行 mockgen 相关生成

```bash
go generate -run "mockgen" ./...
```

### 示例 4: 预览将执行的命令

```bash
go generate -x ./...
```

## 关联命令

- [[go-build|go build]]
- [[mockgen|mockgen]]

## 风险提示

> ⚠️ **MEDIUM**: 执行任意命令（由 //go:generate 定义），审查生成指令

## 最佳实践

[[bp-go-generate|go generate 生产环境最佳实践]]

## 所属维度

[[Go工具链扩展-MOC|编程语言/Go工具链扩展]]
