---
{
  "cmd_name": "tfsec",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://aquasecurity.github.io/tfsec/latest/guides/installation/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "checkov",
    "terraform"
  ],
  "cmd_tags": [
    "safety",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/container/cloudnative/cloudnative-extra.yaml"
}
---

# tfsec

> Terraform 静态安全扫描工具

## 安装

```bash
参考 https://aquasecurity.github.io/tfsec/latest/guides/installation/
```

## 用法

```
tfsec [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--tfvars-file` | 指定变量文件 |
| `--exclude` | 排除检查 |
| `--format` | 输出格式 |

## 示例

### 示例 1: 扫描当前目录 Terraform

```bash
tfsec .
```

### 示例 2: 输出 JSON 报告

```bash
tfsec --format json . > report.json
```

## 关联命令

- [[checkov|checkov]]
- [[terraform|terraform]]

## 风险提示

> ⚠️ **LOW**: 命令风险较低，执行前请阅读文档并确认参数。

## 最佳实践

[[bp-tfsec|tfsec 生产环境最佳实践]]

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
