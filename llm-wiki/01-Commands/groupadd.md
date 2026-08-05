---
{
  "cmd_name": "groupadd",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "groupdel",
    "useradd"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/os/linux-extra.yaml"
}
---

# groupadd

> 创建用户组

## 用法

```
groupadd [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-g` | 指定 GID |
| `-r` | 创建系统组 |

## 示例

### 示例 1: 创建 developers 组

```bash
sudo groupadd developers
```

### 示例 2: 创建指定 GID 的组

```bash
sudo groupadd -g 1001 ops
```

## 关联命令

- [[groupdel|groupdel]]
- [[useradd|useradd]]

## 风险提示

> ⚠️ **MEDIUM**: 会修改系统用户组配置，请确认 GID 不与现有组冲突。

## 最佳实践

[[bp-groupadd|groupadd 生产环境最佳实践]]

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
