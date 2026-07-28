---
{
  "cmd_name": "conftest",
  "cmd_category": "网络工具/安全扫描",
  "cmd_dimension": "安全扫描",
  "cmd_install": "brew install conftest (macOS) 或 go install github.com/open-policy-agent/conftest@latest",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "opa",
    "trivy"
  ],
  "cmd_tags": [
    "safety",
    "docker",
    "kubernetes",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/network/security-tools.yaml"
}
---

# conftest

> 使用 Rego 策略测试配置文件（K8s/Docker/Terraform）

## 安装

```bash
brew install conftest (macOS) 或 go install github.com/open-policy-agent/conftest@latest
```

## 用法

```
conftest test [文件] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `-p` | 策略目录 |
| `--output` | 输出格式 (table/json/junit) |
| `--all-namespaces` | 评估所有命名空间 |

## 示例

### 示例 1: 测试 K8s 配置合规性

```bash
conftest test deployment.yaml
```

### 示例 2: 测试 Terraform 配置

```bash
conftest test -p policies/ terraform/
```

### 示例 3: JSON 格式输出测试结果

```bash
conftest test --output json docker-compose.yml
```

### 示例 4: 测试整个目录

```bash
conftest test -p policies/ k8s/ --all-namespaces
```

## 关联命令

- [[opa|opa]]
- [[trivy|trivy]]

## 风险提示

> ⚠️ **LOW**: 只读测试操作，无风险

## 所属维度

[[安全扫描-MOC|网络工具/安全扫描]]
