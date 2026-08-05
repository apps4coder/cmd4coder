---
{
  "cmd_name": "direnv",
  "cmd_category": "Shell脚本/现代工具",
  "cmd_dimension": "现代工具",
  "cmd_install": "brew install direnv (macOS) 或 apt install direnv (Ubuntu)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "export",
    "source"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/shell/modern-tools.yaml"
}
---

# direnv

> 目录级环境变量自动加载工具

## 安装

```bash
brew install direnv (macOS) 或 apt install direnv (Ubuntu)
```

## 用法

```
direnv allow [路径]
```

```
direnv deny [路径]
```

## 参数

| Flag | Description |
|------|-------------|
| `allow` | 允许加载 .envrc |
| `deny` | 禁止加载 .envrc |
| `edit` | 编辑 .envrc |
| `status` | 查看当前状态 |

## 示例

### 示例 1: 创建并允许环境变量文件

```bash
echo 'export DATABASE_URL=postgres://localhost/dev' > .envrc && direnv allow
```

### 示例 2: 禁止当前目录的 .envrc

```bash
direnv deny
```

### 示例 3: 用编辑器打开 .envrc

```bash
direnv edit
```

### 示例 4: 查看 direnv 加载状态

```bash
direnv status
```

## 关联命令

- [[export|export]]
- [[source|source]]

## 风险提示

> ⚠️ **MEDIUM**: .envrc 可执行任意 shell 命令，仅 allow 可信目录

## 最佳实践

[[bp-direnv|direnv 生产环境最佳实践]]

## 所属维度

[[现代工具-MOC|Shell脚本/现代工具]]
