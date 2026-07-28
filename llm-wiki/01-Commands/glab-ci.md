---
{
  "cmd_name": "glab ci",
  "cmd_category": "CI-CD/平台工具",
  "cmd_dimension": "平台工具",
  "cmd_install": "同 glab",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "glab",
    "glab mr"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cicd/platforms.yaml"
}
---

# glab ci

> 管理 GitLab CI/CD Pipeline

## 安装

```bash
同 glab
```

## 用法

```
glab ci [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `-b` | 指定分支 |
| `--pipeline-id` | Pipeline ID |

## 示例

### 示例 1: 列出最近的 Pipeline

```bash
glab ci list
```

### 示例 2: 查看 main 分支 Pipeline 状态

```bash
glab ci status -b main
```

### 示例 3: 查看 Pipeline 详情

```bash
glab ci view 12345
```

### 示例 4: 重试失败的 Pipeline

```bash
glab ci retry --pipeline-id 12345
```

### 示例 5: 实时跟踪当前 Pipeline 日志

```bash
glab ci trace
```

## 关联命令

- [[glab|glab]]
- [[glab-mr|glab mr]]

## 风险提示

> ⚠️ **LOW**: 查看操作无风险，retry 消耗 Runner 配额

## 所属维度

[[平台工具-MOC|CI-CD/平台工具]]
