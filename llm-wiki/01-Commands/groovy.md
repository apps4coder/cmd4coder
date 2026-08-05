---
{
  "cmd_name": "groovy",
  "cmd_category": "编程语言/扩展工具链",
  "cmd_dimension": "扩展工具链",
  "cmd_install": "SDKMAN 或包管理器安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "java",
    "gradle"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/lang/more.yaml"
}
---

# groovy

> Groovy 脚本语言

## 安装

```bash
SDKMAN 或包管理器安装
```

## 用法

```
groovy [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-v` |  |
| `-e` | 执行 |
| `-classpath` |  |

## 示例

### 示例 1: 查看版本

```bash
groovy -v
```

### 示例 2: 运行脚本

```bash
groovy script.groovy
```

## 关联命令

- [[java|java]]
- [[gradle|gradle]]

## 风险提示

> ⚠️ **LOW**: 命令风险较低，执行前请阅读文档并确认参数。

## 最佳实践

[[bp-groovy|groovy 生产环境最佳实践]]

## 所属维度

[[扩展工具链-MOC|编程语言/扩展工具链]]
