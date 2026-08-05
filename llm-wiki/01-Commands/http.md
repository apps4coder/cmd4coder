---
{
  "cmd_name": "http",
  "cmd_category": "Shell脚本/现代工具",
  "cmd_dimension": "现代工具",
  "cmd_install": "brew install httpie (macOS) 或 pip install httpie",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "curl",
    "rg"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/shell/modern-tools.yaml"
}
---

# http

> HTTPie 人性化 HTTP 客户端（curl 的现代替代）

## 安装

```bash
brew install httpie (macOS) 或 pip install httpie
```

## 用法

```
http [方法] URL [请求项]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | 表单提交 |
| `-a` | 认证 (-a user:pass) |
| `--headers` | 仅显示响应头 |
| `--body` | 仅显示响应体 |
| `-d` | 下载文件 |

## 示例

### 示例 1: GET 请求

```bash
http GET api.example.com/users
```

### 示例 2: POST JSON 数据

```bash
http POST api.example.com/users name=John email=john@example.com
```

### 示例 3: 带 Basic Auth 请求

```bash
http -a admin:secret GET api.example.com/admin
```

### 示例 4: 仅查看响应头

```bash
http --headers GET https://example.com
```

## 关联命令

- [[curl|curl]]
- [[rg|rg]]

## 风险提示

> ⚠️ **MEDIUM**: POST/PUT/DELETE 修改远端数据

## 最佳实践

[[bp-http|http 生产环境最佳实践]]

## 所属维度

[[现代工具-MOC|Shell脚本/现代工具]]
