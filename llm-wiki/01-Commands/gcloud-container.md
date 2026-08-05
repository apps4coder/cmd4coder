---
{
  "cmd_name": "gcloud container",
  "cmd_category": "云平台/GCP CLI",
  "cmd_dimension": "GCP CLI",
  "cmd_install": "同 gcloud",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "gcloud compute",
    "kubectl"
  ],
  "cmd_tags": [
    "kubernetes",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/gcloud.yaml"
}
---

# gcloud container

> 管理 GKE Kubernetes 集群

## 安装

```bash
同 gcloud
```

## 用法

```
gcloud container clusters [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--zone` | 集群所在区域 |
| `--region` | 区域集群 |
| `--num-nodes` | 节点数量 |
| `--machine-type` | 节点机器类型 |

## 示例

### 示例 1: 列出所有 GKE 集群

```bash
gcloud container clusters list
```

### 示例 2: 创建 3 节点 GKE 集群

```bash
gcloud container clusters create my-cluster --num-nodes=3
```

### 示例 3: 获取集群 kubeconfig 凭证

```bash
gcloud container clusters get-credentials my-cluster
```

### 示例 4: 扩容集群至 5 节点

```bash
gcloud container clusters resize my-cluster --num-nodes=5
```

## 关联命令

- [[gcloud-compute|gcloud compute]]
- [[kubectl|kubectl]]

## 风险提示

> ⚠️ **HIGH**: 集群操作涉及费用，resize/delete 影响运行中的工作负载

## 最佳实践

[[bp-gcloud-container|gcloud container 生产环境最佳实践]]

## 所属维度

[[GCP CLI-MOC|云平台/GCP CLI]]
