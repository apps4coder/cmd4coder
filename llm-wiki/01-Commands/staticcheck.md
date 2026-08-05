---
{
  "cmd_name": "staticcheck",
  "cmd_category": "编程语言/Go工具链扩展",
  "cmd_dimension": "Go工具链扩展",
  "cmd_install": "go install honnef.co/go/tools/cmd/staticcheck@latest",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "golangci-lint",
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

# staticcheck

> Go 高级静态分析工具（比 go vet 更深入）

## 安装

```bash
go install honnef.co/go/tools/cmd/staticcheck@latest
```

## 用法

```
staticcheck [选项] [包]
```

## 参数

| Flag | Description |
|------|-------------|
| `-checks` | 选择检查项 |
| `-explain` | 解释检查项 |
| `-json` | JSON 输出 |

## 示例

### 示例 1: 检查所有包

```bash
staticcheck ./...
```

### 示例 2: 启用所有检查

```bash
staticcheck -checks all ./...
```

### 示例 3: 解释弃用 API 检查规则

```bash
staticcheck -explain SA1019
```

### 示例 4: 继承默认但排除 SA1019

```bash
staticcheck -checks "inherit,-SA1019" ./...
```

## 关联命令

- [[golangci-lint|golangci-lint]]
- [[go-vet|go vet]]

## 风险提示

> ⚠️ **LOW**: 只读检查操作，无风险

## 最佳实践

[[bp-staticcheck|staticcheck 生产环境最佳实践]]

## 所属维度

[[Go工具链扩展-MOC|编程语言/Go工具链扩展]]
