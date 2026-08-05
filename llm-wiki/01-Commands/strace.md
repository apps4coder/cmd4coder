---
{
  "cmd_name": "strace",
  "cmd_category": "系统诊断/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "多数 Linux 预装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ltrace",
    "perf"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/diagnostic/more.yaml"
}
---

# strace

> 跟踪系统调用

## 安装

```bash
多数 Linux 预装
```

## 用法

```
strace [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `-e` | 过滤系统调用 |
| `-f` | 跟踪子进程 |
| `-o` | 输出文件 |
| `-p` | 附加 PID |
| `-c` | 统计 |

## 示例

### 示例 1: 统计 ls 的系统调用

```bash
strace -c ls
```

### 示例 2: 跟踪文件 IO

```bash
strace -e openat,read -o trace.log ./app
```

## 关联命令

- [[ltrace|ltrace]]
- [[perf|perf]]

## 风险提示

> ⚠️ **LOW**: 只读/信息查询类操作，风险较低，但仍需确认目标对象与权限。

## 最佳实践

[[bp-strace|strace 生产环境最佳实践]]

## 所属维度

[[扩展工具-MOC|系统诊断/扩展工具]]
