---
{
  "cmd_name": "circleci",
  "cmd_category": "CI/CD/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "参考 https://circleci.com/docs/local-cli/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "github-actions",
    "gitlab-runner"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cicd/more.yaml"
}
---

# circleci

> CircleCI CLI

## 安装

```bash
参考 https://circleci.com/docs/local-cli/
```

## 用法

```
circleci [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `config` | validate |
| `local` | execute |
| `orb` |  |

## 示例

### 示例 1: 验证 config.yml

```bash
circleci config validate
```

### 示例 2: 本地执行 job

```bash
circleci local execute --job test
```

## 关联命令

- [[gitlab-runner|gitlab-runner]]

## 风险提示

> ⚠️ **LOW**: 命令风险较低，执行前请阅读文档并确认参数。

## 最佳实践

[[bp-circleci|circleci 生产环境最佳实践]]

## 所属维度

[[扩展工具-MOC|CI/CD/扩展工具]]
