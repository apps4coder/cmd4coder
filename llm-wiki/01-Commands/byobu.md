---
{
  "cmd_name": "byobu",
  "cmd_category": "Shell脚本/终端复用",
  "cmd_dimension": "终端复用",
  "cmd_install": "brew install byobu (macOS) 或 apt install byobu (Ubuntu)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "tmux",
    "screen"
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

# byobu

> tmux/screen 增强前端，提供状态栏和快捷键

## 安装

```bash
brew install byobu (macOS) 或 apt install byobu (Ubuntu)
```

## 用法

```
byobu [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `-S` | 指定后端 (tmux/screen) |
| `enable` | 登录时自动启动 |
| `disable` | 取消自动启动 |

## 示例

### 示例 1: 启动 byobu 会话

```bash
byobu
```

### 示例 2: SSH 登录时自动启动 byobu

```bash
byobu enable
```

### 示例 3: 打开配置界面

```bash
byobu-config
```

### 示例 4: 查看状态栏信息

```bash
byobu-status
```

## 关联命令

- [[tmux|tmux]]
- [[screen|screen]]

## 风险提示

> ⚠️ **LOW**: 基于 tmux/screen，风险同底层工具

## 最佳实践

[[bp-byobu|byobu 生产环境最佳实践]]

## 所属维度

[[终端复用-MOC|Shell脚本/终端复用]]
