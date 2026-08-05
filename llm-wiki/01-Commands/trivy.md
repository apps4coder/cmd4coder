---
{
  "cmd_name": "trivy",
  "cmd_category": "网络工具/安全扫描",
  "cmd_dimension": "安全扫描",
  "cmd_install": "brew install trivy (macOS) 或 curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "grype",
    "syft"
  ],
  "cmd_tags": [
    "safety",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/network/security-tools.yaml"
}
---

# trivy

> 全能安全扫描器（容器镜像、文件系统、Git 仓库漏洞检测）

## 安装

```bash
brew install trivy (macOS) 或 curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh
```

## 用法

```
trivy [目标类型] [选项] [目标]
```

## 参数

| Flag | Description |
|------|-------------|
| `image` | 扫描容器镜像 |
| `fs` | 扫描文件系统 |
| `repo` | 扫描 Git 仓库 |
| `--severity` | 过滤严重级别 (CRITICAL,HIGH,MEDIUM) |
| `--format` | 输出格式 (table/json/sarif) |
| `--ignore-unfixed` | 忽略无修复方案的漏洞 |

## 示例

### 示例 1: 扫描容器镜像漏洞

```bash
trivy image python:3.12
```

### 示例 2: 扫描当前目录依赖漏洞

```bash
trivy fs --severity CRITICAL,HIGH .
```

### 示例 3: 扫描远程仓库

```bash
trivy repo https://github.com/org/repo
```

### 示例 4: JSON 格式输出报告

```bash
trivy image --format json -o report.json myapp:latest
```

## 关联命令

- [[grype|grype]]
- [[syft|syft]]

## 风险提示

> ⚠️ **LOW**: 只读扫描操作，无风险

## 最佳实践

[[bp-trivy|trivy 生产环境最佳实践]]

## 所属维度

[[安全扫描-MOC|网络工具/安全扫描]]
