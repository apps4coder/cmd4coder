---
{
  "cmd_name": "py-spy",
  "cmd_category": "诊断工具/性能分析",
  "cmd_dimension": "性能分析",
  "cmd_install": "pip install py-spy 或 cargo install py-spy",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "perf",
    "flamegraph"
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

# py-spy

> Python 采样性能分析器（无需修改代码）

## 安装

```bash
pip install py-spy 或 cargo install py-spy
```

## 用法

```
py-spy [命令] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `top` | 实时 top 视图 |
| `record` | 录制火焰图 |
| `dump` | 导出当前调用栈 |
| `-p` | 目标进程 PID |
| `-f` | 输出格式 (flamegraph/speedscope/raw) |

## 示例

### 示例 1: 实时查看 Python 热点函数

```bash
py-spy top -p 1234
```

### 示例 2: 录制 30 秒火焰图

```bash
py-spy record -o flame.svg -p 1234 --duration 30
```

### 示例 3: 导出当前所有线程调用栈

```bash
py-spy dump -p 1234
```

### 示例 4: 启动并分析 Python 程序

```bash
py-spy record -o profile.svg -- python app.py
```

## 关联命令

- [[perf|perf]]
- [[flamegraph|flamegraph]]

## 风险提示

> ⚠️ **LOW**: 采样式分析，对目标进程影响极小

## 最佳实践

[[bp-py-spy|py-spy 生产环境最佳实践]]

## 所属维度

[[性能分析-MOC|诊断工具/性能分析]]
