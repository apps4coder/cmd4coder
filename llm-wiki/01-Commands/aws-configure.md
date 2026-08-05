---
{
  "cmd_name": "aws configure",
  "cmd_category": "云平台/AWS CLI",
  "cmd_dimension": "AWS CLI",
  "cmd_install": "同 aws cli",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "aws",
    "aws sts"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/aws-cli.yaml"
}
---

# aws configure

> 配置 AWS CLI 凭证和默认设置

## 安装

```bash
同 aws cli
```

## 用法

```
aws configure
```

```
aws configure --profile <名称>
```

## 参数

| Flag | Description |
|------|-------------|
| `--profile` | 指定配置文件名称 |

## 示例

### 示例 1: 交互式配置默认凭证

```bash
aws configure
```

### 示例 2: 配置生产环境凭证

```bash
aws configure --profile production
```

### 示例 3: 设置默认区域

```bash
aws configure set region ap-northeast-1
```

## 关联命令

- [[aws|aws]]
- [[aws-sts|aws sts]]

## 风险提示

> ⚠️ **HIGH**: 凭证明文存储在 ~/.aws/credentials，确保文件权限为 600

> ⚠️ **HIGH**: 云资源操作可能产生费用或删除数据，建议先确认区域、账号，并使用 --dry-run 验证。

## 最佳实践

[[bp-aws-configure|aws configure 生产环境最佳实践]]

## 所属维度

[[AWS CLI-MOC|云平台/AWS CLI]]
