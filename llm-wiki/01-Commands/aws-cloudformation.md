---
{
  "cmd_name": "aws cloudformation",
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
    "terraform"
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

# aws cloudformation

> CloudFormation 基础设施即代码管理

## 安装

```bash
同 aws cli
```

## 用法

```
aws cloudformation [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--template-body` | 指定模板内容 |
| `--parameters` | 传递参数 |
| `--capabilities` | 声明模板能力 (CAPABILITY_IAM) |

## 示例

### 示例 1: 部署 CloudFormation 堆栈

```bash
aws cloudformation deploy --template-file template.yaml --stack-name mystack
```

### 示例 2: 查看堆栈状态

```bash
aws cloudformation describe-stacks --stack-name mystack
```

### 示例 3: 删除堆栈

```bash
aws cloudformation delete-stack --stack-name mystack
```

## 关联命令

- [[aws|aws]]
- [[terraform|terraform]]

## 风险提示

> ⚠️ **HIGH**: delete-stack 会删除所有关联资源，操作不可逆

> ⚠️ **HIGH**: 云资源操作可能产生费用或删除数据，建议先确认区域、账号，并使用 --dry-run 验证。

## 最佳实践

[[bp-aws-cloudformation|aws cloudformation 生产环境最佳实践]]

## 所属维度

[[AWS CLI-MOC|云平台/AWS CLI]]
