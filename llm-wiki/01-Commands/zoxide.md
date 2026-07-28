---
{
  "cmd_name": "zoxide",
  "cmd_category": "Shell脚本/现代工具",
  "cmd_dimension": "现代工具",
  "cmd_install": "brew install zoxide (macOS) 或 apt install zoxide (Ubuntu)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cd",
    "fzf"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/shell/modern-tools.yaml"
}
---

# zoxide

> 智能 cd 替代品，记忆常用目录快速跳转

## 安装

```bash
brew install zoxide (macOS) 或 apt install zoxide (Ubuntu)
```

## 用法

```
z [关键词]
```

```
zi [关键词] (交互式)
```

## 参数

| Flag | Description |
|------|-------------|
| `z` | 跳转到最匹配的目录 |
| `zi` | 交互式选择（需 fzf） |
| `z add` | 手动添加目录 |
| `z query` | 查询匹配的目录 |

## 示例

### 示例 1: 跳转到最常访问的含 project 的目录

```bash
z project
```

### 示例 2: 交互式选择目录（fzf 界面）

```bash
zi
```

### 示例 3: 手动添加目录到数据库

```bash
z add /opt/myapp
```

### 示例 4: 查询匹配 proj 的目录列表

```bash
z query proj
```

## 关联命令

- [[cd|cd]]
- [[fzf|fzf]]

## 风险提示

> ⚠️ **LOW**: 仅切换目录，无风险

## 所属维度

[[现代工具-MOC|Shell脚本/现代工具]]
