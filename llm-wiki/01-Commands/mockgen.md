---
{
  "cmd_name": "mockgen",
  "cmd_category": "编程语言/Go工具链扩展",
  "cmd_dimension": "Go工具链扩展",
  "cmd_install": "go install go.uber.org/mock/mockgen@latest",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "go generate",
    "go test"
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

# mockgen

> Go 接口 Mock 代码生成器（单元测试用）

## 安装

```bash
go install go.uber.org/mock/mockgen@latest
```

## 用法

```
mockgen [选项] [包] [接口]
```

## 参数

| Flag | Description |
|------|-------------|
| `-source` | 源模式（从文件生成） |
| `-destination` | 输出文件 |
| `-package` | 输出包名 |
| `-mock_names` | 自定义 Mock 名称 |

## 示例

### 示例 1: 从源文件生成 Mock

```bash
mockgen -source=internal/service/user.go -destination=internal/service/mock_user.go -package=service
```

### 示例 2: 从包路径生成 Mock

```bash
mockgen -destination=mocks/mock_db.go -package=mocks github.com/org/repo/internal/db Repository
```

### 示例 3: 自定义 Mock 类型名

```bash
mockgen -source=handler.go -destination=mock_handler.go -mock_names=Handler=MockHandler
```

## 关联命令

- [[go-generate|go generate]]
- [[go-test|go test]]

## 风险提示

> ⚠️ **LOW**: 代码生成操作，无风险

## 所属维度

[[Go工具链扩展-MOC|编程语言/Go工具链扩展]]
