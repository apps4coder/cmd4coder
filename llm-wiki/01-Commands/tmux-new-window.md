---
{
  "cmd_name": "tmux new-window",
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
    "tmux split-window"
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

# tmux new-window

> tmux 窗口和标签页管理

## 安装

```bash
同 tmux
```

## 用法

```
Ctrl+b c (新建窗口)
```

```
Ctrl+b n/p (切换窗口)
```

## 参数

| Flag | Description |
|------|-------------|
| `Ctrl+b c` | 创建新窗口 |
| `Ctrl+b n` | 切换到下一个窗口 |
| `Ctrl+b p` | 切换到上一个窗口 |
| `Ctrl+b 数字` | 切换到指定编号窗口 |
| `Ctrl+b ,` | 重命名当前窗口 |
| `Ctrl+b &` | 关闭当前窗口 |

## 示例

### 示例 1: 新建一个窗口标签

```bash
Ctrl+b c
```

### 示例 2: 跳转到 2 号窗口

```bash
Ctrl+b 2
```

### 示例 3: 重命名窗口为有意义的名称

```bash
Ctrl+b ,
```

### 示例 4: 命令行方式重命名窗口

```bash
tmux rename-window -t dev "build"
```

## 关联命令

- [[tmux|tmux]]
- [[tmux-split-window|tmux split-window]]

## 风险提示

> ⚠️ **LOW**: 关闭窗口终止其中所有进程

## 所属维度

[[终端复用-MOC|Shell脚本/终端复用]]
