---
{
  "cmd_name": "bun",
  "cmd_category": "构建工具/包管理",
  "cmd_dimension": "包管理",
  "cmd_install": "curl -fsSL https://bun.sh/install | bash 或 brew install oven-sh/bun/bun (macOS)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "pnpm",
    "npm"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/build-tools/pkg-mgmt.yaml"
}
---

# bun

> 极速 JavaScript 运行时、包管理器和打包器

## 安装

```bash
curl -fsSL https://bun.sh/install | bash 或 brew install oven-sh/bun/bun (macOS)
```

## 用法

```
bun [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `install` | 安装依赖 |
| `run` | 运行脚本 |
| `add` | 添加包 |
| `x` | 执行包命令 |

## 示例

### 示例 1: 极速安装依赖（比 npm 快 10-30x）

```bash
bun install
```

### 示例 2: 运行 package.json 中的 dev 脚本

```bash
bun run dev
```

### 示例 3: 添加依赖

```bash
bun add express
```

### 示例 4: 执行包命令

```bash
bun x create-vite my-app
```

### 示例 5: 打包 TypeScript

```bash
bun build src/index.ts --outdir dist
```

## 关联命令

- [[pnpm|pnpm]]
- [[npm|npm]]

## 风险提示

> ⚠️ **LOW**: 包管理和构建操作风险低

## 所属维度

[[包管理-MOC|构建工具/包管理]]
