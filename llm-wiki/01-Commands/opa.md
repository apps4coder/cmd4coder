---
{
  "cmd_name": "opa",
  "cmd_category": "网络工具/安全扫描",
  "cmd_dimension": "安全扫描",
  "cmd_install": "brew install opa (macOS) 或 curl -L -o opa https://openpolicyagent.org/downloads/latest/opa_linux_amd64_static",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "trivy",
    "conftest"
  ],
  "cmd_tags": [
    "safety",
    "agent",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/network/security-tools.yaml"
}
---

# opa

> Open Policy Agent 策略即代码引擎

## 安装

```bash
brew install opa (macOS) 或 curl -L -o opa https://openpolicyagent.org/downloads/latest/opa_linux_amd64_static
```

## 用法

```
opa [命令] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `eval` | 评估 Rego 策略 |
| `test` | 运行策略测试 |
| `fmt` | 格式化 Rego 文件 |
| `run` | 启动 OPA 服务器 |

## 示例

### 示例 1: 评估策略

```bash
opa eval -d policy.rego -i input.json "data.authz.allow"
```

### 示例 2: 运行策略单元测试

```bash
opa test ./policies/ -v
```

### 示例 3: 格式化策略文件

```bash
opa fmt -w policy.rego
```

### 示例 4: 启动 OPA 决策服务器

```bash
opa run --server --addr :8181
```

## 关联命令

- [[trivy|trivy]]
- [[conftest|conftest]]

## 风险提示

> ⚠️ **LOW**: 策略评估操作风险低

## 最佳实践

[[bp-opa|opa 生产环境最佳实践]]

## 所属维度

[[安全扫描-MOC|网络工具/安全扫描]]
