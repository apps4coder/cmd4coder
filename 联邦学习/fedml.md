---
{
  "cmd_name": "fedml",
  "cmd_category": "AI基础设施/联邦学习",
  "cmd_dimension": "联邦学习",
  "cmd_install": "pip install fedml",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "flower",
    "nvflare"
  ],
  "cmd_tags": [
    "training",
    "federated",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/federated-learning.yaml"
}
---

# fedml

> FedML 跨设备联邦学习平台，支持端-边-云协同、多种拓扑与异构训练

## 安装

```bash
pip install fedml
```

## 用法

```
fedml [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `login` | 登录FedML平台 |
| `launch` | 启动联邦训练作业 |
| `run` | 本地/集群运行训练脚本 |

## 示例

### 示例 1: 登录平台并绑定设备

```bash
fedml login <api_key>
```

### 示例 2: 根据配置启动联邦训练job

```bash
fedml launch job.yaml
```

## 关联命令

- [[flower|flower]]
- [[nvflare|nvflare]]

## 风险提示

> ⚠️ **LOW**: 使用托管平台时训练元数据上传至SaaS，需评估数据合规

## 参考链接

- [https://doc.fedml.ai/](https://doc.fedml.ai/)

## 所属维度

[[联邦学习-MOC|AI基础设施/联邦学习]]
