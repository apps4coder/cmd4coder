---
{
  "cmd_name": "tmux split-window",
  "cmd_category": "Shell脚本/终端复用",
  "cmd_dimension": "终端复用",
  "cmd_install": "同 tmux",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "tmux",
    "tmux new-window"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/shell/tmux.yaml"
}
---

# tmux split-window

> tmux 窗口分割和面板管理（前缀键 Ctrl+b）

## 安装

```bash
同 tmux
```

## 用法

```
Ctrl+b % (垂直分割)
```

```
Ctrl+b " (水平分割)
```

## 参数

| Flag | Description |
|------|-------------|
| `Ctrl+b %` | 垂直分割当前窗格 |
| `Ctrl+b "` | 水平分割当前窗格 |
| `Ctrl+b 方向键` | 在窗格间切换 |
| `Ctrl+b x` | 关闭当前窗格 |
| `Ctrl+b z` | 最大化/还原当前窗格 |

## 示例

### 示例 1: 垂直分割，左右两个终端

```bash
Ctrl+b %
```

### 示例 2: 水平分割，上下两个终端

```bash
Ctrl+b "
```

### 示例 3: 临时最大化当前窗格（再按还原）

```bash
Ctrl+b z
```

### 示例 4: 将当前窗格左移

```bash
Ctrl+b {
```

## 关联命令

- [[tmux|tmux]]
- [[tmux-new-window|tmux new-window]]

## 风险提示

> ⚠️ **LOW**: 关闭窗格会终止其中运行的进程

## 最佳实践

[[bp-tmux-split-window|tmux split-window 生产环境最佳实践]]

## 所属维度

[[终端复用-MOC|Shell脚本/终端复用]]
