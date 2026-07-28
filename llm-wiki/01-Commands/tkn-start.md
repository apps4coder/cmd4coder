---
{
  "cmd_name": "tkn start",
  "cmd_category": "CI-CD/平台工具",
  "cmd_dimension": "平台工具",
  "cmd_install": "同 tkn",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "tkn pipelinerun",
    "kubectl"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/cicd/platforms.yaml"
}
---

# tkn start

> 启动 Tekton Pipeline 运行

## 安装

```bash
同 tkn
```

## 用法

```
tkn pipeline start [Pipeline名] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `-p` | 传入参数 (-p name=value) |
| `-w` | 工作空间绑定 |
| `-s` | ServiceAccount |
| `--use-param-defaults` | 使用参数默认值 |

## 示例

### 示例 1: 传参启动 Pipeline

```bash
tkn pipeline start build-deploy -p git-url=https://github.com/org/repo -p image=registry/app:v1
```

### 示例 2: 使用默认参数+工作空间启动

```bash
tkn pipeline start ci --use-param-defaults -w name=shared,pvc=ci-pvc
```

### 示例 3: 启动并实时显示日志

```bash
tkn pipeline start test -s pipeline-sa --showlog
```

## 关联命令

- [[kubectl|kubectl]]

## 风险提示

> ⚠️ **MEDIUM**: 启动 Pipeline 消耗集群资源

## 所属维度

[[平台工具-MOC|CI-CD/平台工具]]
