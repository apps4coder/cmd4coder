---
{
  "cmd_name": "dlv",
  "cmd_category": "编程语言/Go工具链扩展",
  "cmd_dimension": "Go工具链扩展",
  "cmd_install": "go install github.com/go-delve/delve/cmd/dlv@latest",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "go test",
    "gopls"
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

# dlv

> Go 调试器（断点、单步、变量检查）

## 安装

```bash
go install github.com/go-delve/delve/cmd/dlv@latest
```

## 用法

```
dlv [命令] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `debug` | 调试当前包 |
| `attach` | 附加到进程 |
| `exec` | 调试二进制 |
| `test` | 调试测试 |

## 示例

### 示例 1: 调试启动服务

```bash
dlv debug ./cmd/server
```

### 示例 2: 附加到运行中的进程

```bash
dlv attach $(pidof myapp)
```

### 示例 3: 调试测试

```bash
dlv test ./internal/service/
```

### 示例 4: 调试编译好的二进制

```bash
dlv exec ./bin/myapp -- --config prod.yaml
```

## 关联命令

- [[go-test|go test]]
- [[gopls|gopls]]

## 风险提示

> ⚠️ **LOW**: 调试操作，attach 会暂停目标进程

## 最佳实践

[[bp-dlv|dlv 生产环境最佳实践]]

## 所属维度

[[Go工具链扩展-MOC|编程语言/Go工具链扩展]]
