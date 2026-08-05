---
{
  "cmd_name": "gcloud compute",
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
    "gcloud",
    "gcloud container"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cloud/gcloud.yaml"
}
---

# gcloud compute

> 管理 GCE 虚拟机实例、磁盘、网络等计算资源

## 安装

```bash
同 gcloud
```

## 用法

```
gcloud compute [子命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--zone` | 指定实例所在区域 |
| `--machine-type` | 指定机器类型 (e2-medium/n2-standard-2) |
| `--image-family` | 指定操作系统镜像族 |

## 示例

### 示例 1: 列出所有虚拟机实例

```bash
gcloud compute instances list
```

### 示例 2: 创建虚拟机实例

```bash
gcloud compute instances create my-vm --machine-type=e2-medium --zone=us-central1-a
```

### 示例 3: SSH 连接到实例

```bash
gcloud compute ssh my-vm --zone=us-central1-a
```

### 示例 4: 删除虚拟机实例

```bash
gcloud compute instances delete my-vm --zone=us-central1-a
```

## 关联命令

- [[gcloud|gcloud]]
- [[gcloud-container|gcloud container]]

## 风险提示

> ⚠️ **HIGH**: delete 操作不可逆，创建实例会产生费用

## 最佳实践

[[bp-gcloud-compute|gcloud compute 生产环境最佳实践]]

## 所属维度

[[GCP CLI-MOC|云平台/GCP CLI]]
