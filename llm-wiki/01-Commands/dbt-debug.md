---
{
  "cmd_name": "dbt debug",
  "cmd_category": "大数据/调度与转换",
  "cmd_dimension": "调度与转换",
  "cmd_install": "同 dbt",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "dbt"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/bigdata/orchestration.yaml"
}
---

# dbt debug

> 调试 dbt 项目配置和连接

## 安装

```bash
同 dbt
```

## 用法

```
dbt debug [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--config-dir` | 显示配置目录 |
| `--profiles-dir` | 指定 profiles 目录 |

## 示例

### 示例 1: 检查项目配置和数据库连接

```bash
dbt debug
```

### 示例 2: 显示 dbt 配置路径

```bash
dbt debug --config-dir
```

### 示例 3: 列出项目中所有资源

```bash
dbt ls
```

### 示例 4: 生成并预览文档

```bash
dbt docs generate && dbt docs serve
```

## 关联命令

- [[dbt|dbt]]

## 风险提示

> ⚠️ **LOW**: 调试和查看操作无风险

## 最佳实践

[[bp-dbt-debug|dbt debug 生产环境最佳实践]]

## 所属维度

[[调度与转换-MOC|大数据/调度与转换]]
