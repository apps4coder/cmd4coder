---
{
  "cmd_name": "syft",
  "cmd_category": "网络工具/安全扫描",
  "cmd_dimension": "安全扫描",
  "cmd_install": "brew install syft (macOS) 或 curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "grype",
    "trivy"
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

# syft

> 软件物料清单（SBOM）生成工具

## 安装

```bash
brew install syft (macOS) 或 curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh
```

## 用法

```
syft [来源] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `-o` | 输出格式 (syft-json/cyclonedx-json/spdx-json) |
| `--file` | 输出到文件 |
| `packages` | 列出包 |

## 示例

### 示例 1: 生成镜像 SBOM

```bash
syft myapp:latest
```

### 示例 2: 生成 CycloneDX 格式 SBOM

```bash
syft dir:. -o cyclonedx-json > sbom.json
```

### 示例 3: 生成 SPDX 格式 SBOM

```bash
syft myapp:latest -o spdx-json > spdx.json
```

### 示例 4: 列出目录中所有包

```bash
syft packages dir:.
```

## 关联命令

- [[grype|grype]]
- [[trivy|trivy]]

## 风险提示

> ⚠️ **LOW**: 只读操作，无风险

## 最佳实践

[[bp-syft|syft 生产环境最佳实践]]

## 所属维度

[[安全扫描-MOC|网络工具/安全扫描]]
