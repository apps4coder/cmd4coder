---
{
  "cmd_name": "go tool pprof",
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
    "go test -bench",
    "perf"
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

# go tool pprof

> Go 性能分析工具（CPU/内存/goroutine 热点）

## 用法

```
go tool pprof [选项] [profile文件]
```

```
import _ "net/http/pprof" 后访问 /debug/pprof/
```

## 参数

| Flag | Description |
|------|-------------|
| `-http` | 启动 Web UI |
| `-top` | 显示 Top 函数 |
| `-list` | 按源码行显示 |
| `-svg` | 生成调用图 SVG |

## 示例

### 示例 1: Web UI 查看 CPU profile

```bash
go tool pprof -http=:8080 cpu.prof
```

### 示例 2: 查看内存分配 Top 函数

```bash
go tool pprof -top mem.prof
```

### 示例 3: 采集运行中服务 30 秒 CPU profile

```bash
curl -o cpu.prof http://localhost:6060/debug/pprof/profile?seconds=30
```

### 示例 4: 按源码行查看热点

```bash
go tool pprof -list=HandlerFunc cpu.prof
```

## 关联命令

- [[perf|perf]]

## 风险提示

> ⚠️ **LOW**: 只读分析操作，采集 profile 有轻微开销

## 最佳实践

[[bp-go-tool-pprof|go tool pprof 生产环境最佳实践]]

## 所属维度

[[Go工具链扩展-MOC|编程语言/Go工具链扩展]]
