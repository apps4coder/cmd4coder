---
{
  "cmd_name": "pnpm",
  "cmd_category": "构建工具/包管理",
  "cmd_dimension": "包管理",
  "cmd_install": "npm install -g pnpm 或 brew install pnpm (macOS)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "npm",
    "yarn"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/build-tools/pkg-mgmt.yaml"
}
---

# pnpm

> 高性能 Node.js 包管理器（硬链接节省磁盘）

## 安装

```bash
npm install -g pnpm 或 brew install pnpm (macOS)
```

## 用法

```
pnpm [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--filter` | 过滤 workspace 包 |
| `--recursive` | 递归执行 |
| `--frozen-lockfile` | 锁定依赖（CI 推荐） |

## 示例

### 示例 1: 安装依赖

```bash
pnpm install
```

### 示例 2: 添加生产依赖

```bash
pnpm add react --save
```

### 示例 3: 添加开发依赖

```bash
pnpm add -D vitest eslint
```

### 示例 4: 仅构建 workspace 中的 web 包

```bash
pnpm --filter @app/web build
```

### 示例 5: 临时执行包命令（类似 npx）

```bash
pnpm dlx create-next-app
```

## 关联命令

- [[npm|npm]]
- [[yarn|yarn]]

## 风险提示

> ⚠️ **LOW**: 包管理操作风险低

## 最佳实践

[[bp-pnpm|pnpm 生产环境最佳实践]]

## 所属维度

[[包管理-MOC|构建工具/包管理]]
