---
{
  "cmd_name": "screen",
  "cmd_category": "Shell脚本/终端复用",
  "cmd_dimension": "终端复用",
  "cmd_install": "apt install screen (Ubuntu) 或 brew install screen (macOS)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "tmux"
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

# screen

> 经典终端复用器，支持会话保持和恢复

## 安装

```bash
apt install screen (Ubuntu) 或 brew install screen (macOS)
```

## 用法

```
screen [选项] [会话名]
```

## 参数

| Flag | Description |
|------|-------------|
| `-S` | 创建命名会话 |
| `-r` | 恢复分离的会话 |
| `-ls` | 列出所有会话 |
| `-d` | 先分离再恢复 |
| `-x` | 多终端共享会话 |

## 示例

### 示例 1: 创建名为 build 的会话

```bash
screen -S build
```

### 示例 2: 恢复 build 会话

```bash
screen -r build
```

### 示例 3: 列出所有会话

```bash
screen -ls
```

### 示例 4: 强制分离并恢复（会话被其他终端占用时）

```bash
screen -d -r build
```

## 关联命令

- [[tmux|tmux]]

## 风险提示

> ⚠️ **LOW**: kill 会话终止其中进程

## 所属维度

[[终端复用-MOC|Shell脚本/终端复用]]
