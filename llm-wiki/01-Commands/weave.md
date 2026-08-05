---
{
  "cmd_name": "weave",
  "cmd_category": "AI基础设施/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "pip install weave",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "wandb",
    "mlflow"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/more.yaml"
}
---

# weave

> Weights & Biases Weave 可观测工具

## 安装

```bash
pip install weave
```

## 用法

```
weave [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `init` |  |
| `trace` |  |
| `eval` |  |

## 示例

### 示例 1: 初始化项目

```bash
weave.init('project')
```

### 示例 2: 追踪函数调用

```bash
weave trace my_function()
```

## 关联命令

- [[wandb|wandb]]
- [[mlflow|mlflow]]

## 风险提示

> ⚠️ **LOW**: 命令风险较低，执行前请阅读文档并确认参数。

## 参考链接

- [https://weave-docs.wandb.ai/](https://weave-docs.wandb.ai/)
- [https://github.com/wandb/weave](https://github.com/wandb/weave)

## 最佳实践

[[bp-weave|weave 生产环境最佳实践]]

## 所属维度

[[扩展命令-MOC|AI基础设施/扩展命令]]
