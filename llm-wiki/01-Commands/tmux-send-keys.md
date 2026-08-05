---
{
  "cmd_name": "tmux send-keys",
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
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/shell/tmux.yaml"
}
---

# tmux send-keys

> 向 tmux 窗格发送命令（脚本化自动操作）

## 安装

```bash
同 tmux
```

## 用法

```
tmux send-keys -t [目标] [命令] [按键]
```

## 参数

| Flag | Description |
|------|-------------|
| `-t` | 目标窗格 (session:window.pane) |
| `C-m` | 发送回车（执行命令） |
| `-l` | 字面发送（不解析特殊键） |

## 示例

### 示例 1: 在 dev 会话 0 号窗口右侧面板启动开发服务器

```bash
tmux send-keys -t dev:0.1 "npm run dev" C-m
```

### 示例 2: 在左侧面板启动 Go 服务

```bash
tmux send-keys -t dev:0.0 "go run ." C-m
```

### 示例 3: 后台创建会话并执行测试

```bash
tmux new-session -d -s ci && tmux send-keys -t ci "make test" C-m
```

## 关联命令

- [[tmux|tmux]]
- [[tmux-split-window|tmux split-window]]

## 风险提示

> ⚠️ **MEDIUM**: 自动发送命令可能在错误窗格执行危险操作

## 最佳实践

[[bp-tmux-send-keys|tmux send-keys 生产环境最佳实践]]

## 所属维度

[[终端复用-MOC|Shell脚本/终端复用]]
