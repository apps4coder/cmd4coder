---
{
  "cmd_name": "async-profiler",
  "cmd_category": "诊断工具/性能分析",
  "cmd_dimension": "性能分析",
  "cmd_install": "从 GitHub releases 下载或 brew install async-profiler (macOS)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "jstack",
    "perf"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/diagnostic/profiling.yaml"
}
---

# async-profiler

> Java 低开销异步性能分析器（CPU/内存/锁）

## 安装

```bash
从 GitHub releases 下载或 brew install async-profiler (macOS)
```

## 用法

```
./asprof [选项] [PID]
```

## 参数

| Flag | Description |
|------|-------------|
| `-e` | 事件类型 (cpu/alloc/lock/wall) |
| `-d` | 持续时间（秒） |
| `-f` | 输出文件 |
| `-o` | 输出格式 (flamegraph/collapsed/jfr) |

## 示例

### 示例 1: 采集 30 秒 CPU 火焰图

```bash
./asprof -e cpu -d 30 -f flame.html 1234
```

### 示例 2: 采集内存分配火焰图

```bash
./asprof -e alloc -d 60 -f alloc.html 1234
```

### 示例 3: 采集锁竞争火焰图

```bash
./asprof -e lock -d 30 -f lock.html 1234
```

### 示例 4: Wall-clock 模式（含等待时间）

```bash
./asprof -e wall -t -d 30 -f wall.html 1234
```

## 关联命令

- [[jstack|jstack]]
- [[perf|perf]]

## 风险提示

> ⚠️ **LOW**: 异步采样，对 JVM 影响极小（<5%）

## 最佳实践

[[bp-async-profiler|async-profiler 生产环境最佳实践]]

## 所属维度

[[性能分析-MOC|诊断工具/性能分析]]
