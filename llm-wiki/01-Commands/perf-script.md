---
{
  "cmd_name": "perf script",
  "cmd_category": "诊断工具/性能分析",
  "cmd_dimension": "性能分析",
  "cmd_install": "同 perf",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "perf",
    "flamegraph"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/diagnostic/profiling.yaml"
}
---

# perf script

> 导出 perf 采样数据为文本（用于生成火焰图）

## 安装

```bash
同 perf
```

## 用法

```
perf script [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 输入 perf.data 文件 |
| `-F` | 输出字段 |

## 示例

### 示例 1: 导出采样数据

```bash
perf script > perf.out
```

### 示例 2: 生成火焰图完整管道

```bash
perf script -i perf.data | stackcollapse-perf.pl | flamegraph.pl > flame.svg
```

### 示例 3: 自定义输出字段

```bash
perf script -F comm,pid,tid,cpu,time,period,event,ip,sym,dso,trace
```

## 关联命令

- [[perf|perf]]
- [[flamegraph|flamegraph]]

## 风险提示

> ⚠️ **LOW**: 只读操作

## 最佳实践

[[bp-perf-script|perf script 生产环境最佳实践]]

## 所属维度

[[性能分析-MOC|诊断工具/性能分析]]
