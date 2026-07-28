---
{
  "cmd_name": "numastat",
  "cmd_category": "硬件/系统信息",
  "cmd_dimension": "系统信息",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "numactl",
    "free"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/hardware/info.yaml"
}
---

# numastat

> 显示每个 NUMA 节点的内存统计

## 用法

```
numastat [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-m` | 显示 MB |
| `-n` | 节点级 |
| `-c` | 紧凑 |

## 示例

### 示例 1: 查看 NUMA 内存统计

```bash
numastat
```

### 示例 2: 以 MB 显示节点级统计

```bash
numastat -m -n
```

## 关联命令

- [[numactl|numactl]]
- [[free|free]]

## 风险提示

> ⚠️ **LOW**: 只读/信息查询类操作，风险较低，但仍需确认目标对象与权限。

## 所属维度

[[系统信息-MOC|硬件/系统信息]]
