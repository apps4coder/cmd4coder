---
{
  "cmd_name": "gopls",
  "cmd_category": "编程语言/Go工具链扩展",
  "cmd_dimension": "Go工具链扩展",
  "cmd_install": "go install golang.org/x/tools/gopls@latest",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "golangci-lint",
    "dlv"
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

# gopls

> Go 官方语言服务器（IDE 智能补全、跳转、重构）

## 安装

```bash
go install golang.org/x/tools/gopls@latest
```

## 用法

```
gopls [命令] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `version` | 查看版本 |
| `-rpc.trace` | 追踪 RPC 通信 |
| `check` | 检查文件 |

## 示例

### 示例 1: 查看 gopls 版本

```bash
gopls version
```

### 示例 2: 检查文件诊断信息

```bash
gopls check main.go
```

### 示例 3: 调试模式启动（排查 IDE 问题）

```bash
gopls -rpc.trace -v
```

### 示例 4: 更新到最新版本

```bash
go install golang.org/x/tools/gopls@latest
```

## 关联命令

- [[golangci-lint|golangci-lint]]
- [[dlv|dlv]]

## 风险提示

> ⚠️ **LOW**: 语言服务器操作，无风险

## 最佳实践

[[bp-gopls|gopls 生产环境最佳实践]]

## 所属维度

[[Go工具链扩展-MOC|编程语言/Go工具链扩展]]
