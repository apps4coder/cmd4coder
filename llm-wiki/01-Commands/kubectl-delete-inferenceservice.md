---
{
  "cmd_name": "kubectl delete inferenceservice",
  "cmd_category": "Kubernetes MLOps",
  "cmd_dimension": "Kubernetes MLOps",
  "cmd_install": "Requires KServe CRDs installed",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/container/k8s/k8s-mlops.yaml"
}
---

# kubectl delete inferenceservice

> Delete a KServe InferenceService

## 安装

```bash
Requires KServe CRDs installed
```

## 用法

```
kubectl delete inferenceservice <name> [flags]
```

```
kubectl delete isvc <name> [flags]
```

## 示例

### 示例 1: Delete sklearn-iris inference service

```bash
kubectl delete isvc sklearn-iris
```

### 示例 2: Delete all inference services in staging namespace

```bash
kubectl delete isvc -n staging --all
```

## 风险提示

> ⚠️ **HIGH**: Permanently deletes model serving resources

> ⚠️ **HIGH**: 删除推理服务会中断线上流量，建议先完成流量切换或灰度验证。

## 最佳实践

[[bp-kubectl-delete-inferenceservice|kubectl delete inferenceservice 生产环境最佳实践]]

## 所属维度

[[Kubernetes MLOps-MOC|Kubernetes MLOps]]
