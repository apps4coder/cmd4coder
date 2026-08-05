---
{
  "cmd_name": "flamegraph",
  "cmd_category": "诊断工具/性能分析",
  "cmd_dimension": "性能分析",
  "cmd_install": "git clone https://github.com/brendangregg/FlameGraph 或 brew install flamegraph (macOS)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "perf",
    "py-spy"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/diagnostic/profiling.yaml"
}
---

# flamegraph

> 火焰图生成工具（可视化性能热点）

## 安装

```bash
git clone https://github.com/brendangregg/FlameGraph 或 brew install flamegraph (macOS)
```

## 用法

```
stackcollapse-*.pl < input | flamegraph.pl > output.svg
```

## 参数

| Flag | Description |
|------|-------------|
| `--title` | 图表标题 |
| `--width` | 输出宽度 |
| `--colors` | 配色方案 (hot/java/mem) |
| `--reverse` | 反转（冰柱图） |

## 示例

### 示例 1: 从 perf 数据生成 CPU 火焰图

```bash
perf script | stackcollapse-perf.pl | flamegraph.pl > cpu.svg
```

### 示例 2: 内存配色火焰图

```bash
perf script | stackcollapse-perf.pl | flamegraph.pl --colors mem > mem.svg
```

### 示例 3: Python 火焰图

```bash
py-spy record -f raw -p 1234 | stackcollapse-perf.pl | flamegraph.pl > py.svg
```

### 示例 4: 自定义标题和宽度

```bash
cat collapsed.txt | flamegraph.pl --title "My App" --width 1600 > out.svg
```

## 关联命令

- [[perf|perf]]
- [[py-spy|py-spy]]

## 风险提示

> ⚠️ **LOW**: 离线数据处理，无风险

## 最佳实践

[[bp-flamegraph|flamegraph 生产环境最佳实践]]

## 所属维度

[[性能分析-MOC|诊断工具/性能分析]]
