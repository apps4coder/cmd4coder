---
{
  "cmd_name": "dagger",
  "cmd_category": "CI-CD/平台工具",
  "cmd_dimension": "平台工具",
  "cmd_install": "brew install dagger/tap/dagger (macOS) 或 curl -L https://dl.dagger.io/dagger/install.sh | sh",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "act",
    "tkn"
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

# dagger

> Dagger 可编程 CI/CD 引擎，用代码定义 Pipeline

## 安装

```bash
brew install dagger/tap/dagger (macOS) 或 curl -L https://dl.dagger.io/dagger/install.sh | sh
```

## 用法

```
dagger [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--output` | 输出目录 |
| `--progress` | 进度显示模式 (plain/tty) |

## 示例

### 示例 1: 初始化 Dagger 模块（Go SDK）

```bash
dagger init --sdk=go
```

### 示例 2: 执行模块中的 build 函数

```bash
dagger call build
```

### 示例 3: 执行测试并输出结果

```bash
dagger call test --output=./results
```

### 示例 4: 执行部署函数

```bash
dagger call deploy --image=registry/app:v1
```

## 关联命令

- [[act|act]]
- [[tkn|tkn]]

## 风险提示

> ⚠️ **MEDIUM**: Pipeline 中可能执行部署操作

## 所属维度

[[平台工具-MOC|CI-CD/平台工具]]
