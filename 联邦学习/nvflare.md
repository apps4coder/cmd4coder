---
{
  "cmd_name": "nvflare",
  "cmd_category": "AI基础设施/联邦学习",
  "cmd_dimension": "联邦学习",
  "cmd_install": "pip install nvflare",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "flower",
    "opacus"
  ],
  "cmd_tags": [
    "deployment",
    "safety",
    "federated",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/federated-learning.yaml"
}
---

# nvflare

> NVIDIA FLARE 企业级联邦学习SDK，支持横/纵向联邦、安全聚合与医疗/金融场景部署

## 安装

```bash
pip install nvflare
```

## 用法

```
nvflare [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `simulator` | 本地模拟多客户端联邦训练 |
| `provision` | 生成客户端/服务端启动包与证书 |
| `job submit` | 向联邦系统提交训练job |

## 示例

### 示例 1: 模拟2客户端联邦训练

```bash
nvflare simulator -w /tmp/nvflare -n 2 -t 2 job_folder
```

### 示例 2: 根据项目配置生成部署包与TLS证书

```bash
nvflare provision -p project.yml
```

## 关联命令

- [[flower|flower]]
- [[opacus|opacus]]

## 风险提示

> ⚠️ **MEDIUM**: 跨机构部署需正确分发证书，证书泄露会破坏联邦信任链

## 参考链接

- [https://nvflare.readthedocs.io/](https://nvflare.readthedocs.io/)

## 最佳实践

[[bp-nvflare|nvflare 生产环境最佳实践]]

## 所属维度

[[联邦学习-MOC|AI基础设施/联邦学习]]
