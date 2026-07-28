---
{
  "cmd_name": "npm",
  "cmd_category": "构建工具/包管理",
  "cmd_dimension": "包管理",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "pnpm",
    "bun"
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

# npm

> Node.js 默认包管理器

## 用法

```
npm [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `install / i` | 安装依赖 |
| `run` | 运行 package.json 脚本 |
| `-g` | 全局安装 |
| `--save-dev / -D` | 保存为开发依赖 |
| `ci` | 干净安装（CI 推荐） |

## 示例

### 示例 1: 安装所有依赖

```bash
npm install
```

### 示例 2: 干净安装（删除 node_modules 后安装）

```bash
npm ci
```

### 示例 3: 运行 build 脚本

```bash
npm run build
```

### 示例 4: 安装开发依赖

```bash
npm install -D vitest
```

### 示例 5: 自动修复安全漏洞

```bash
npm audit fix
```

## 关联命令

- [[pnpm|pnpm]]
- [[bun|bun]]

## 风险提示

> ⚠️ **LOW**: 包管理操作风险低，audit fix 可能升级破坏性版本

## 所属维度

[[包管理-MOC|构建工具/包管理]]
