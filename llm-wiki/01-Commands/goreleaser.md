---
{
  "cmd_name": "goreleaser",
  "cmd_category": "CI-CD/平台工具",
  "cmd_dimension": "平台工具",
  "cmd_install": "brew install goreleaser (macOS) 或 go install github.com/goreleaser/goreleaser/v2@latest",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "gh release",
    "make"
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

# goreleaser

> Go 项目自动化发布工具（构建、打包、发布）

## 安装

```bash
brew install goreleaser (macOS) 或 go install github.com/goreleaser/goreleaser/v2@latest
```

## 用法

```
goreleaser [命令] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--snapshot` | 快照模式（不发布，仅本地构建） |
| `--clean` | 清理 dist 目录 |
| `--skip` | 跳过步骤 (publish/validate/announce) |
| `--config` | 指定配置文件 |

## 示例

### 示例 1: 本地快照构建（不发布）

```bash
goreleaser release --snapshot --clean
```

### 示例 2: 正式构建并发布到 GitHub Releases

```bash
goreleaser release --clean
```

### 示例 3: 仅构建当前平台

```bash
goreleaser build --single-target
```

### 示例 4: 验证配置文件

```bash
goreleaser check
```

## 关联命令

- [[gh-release|gh release]]
- [[make|make]]

## 风险提示

> ⚠️ **MEDIUM**: release 会推送到 GitHub Releases，确认版本号正确

## 最佳实践

[[bp-goreleaser|goreleaser 生产环境最佳实践]]

## 所属维度

[[平台工具-MOC|CI-CD/平台工具]]
