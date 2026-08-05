---
{
  "cmd_name": "named-checkconf",
  "cmd_category": "网络工具/基础设施",
  "cmd_dimension": "基础设施",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "rndc",
    "dnsmasq"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/network/infra.yaml"
}
---

# named-checkconf

> 检查 BIND DNS 配置文件语法

## 用法

```
named-checkconf [OPTIONS] [FILE]
```

## 参数

| Flag | Description |
|------|-------------|
| `-z` | 检查所有 zone |
| `-p` | 打印配置 |
| `-t` | 指定 chroot |

## 示例

### 示例 1: 检查 named.conf

```bash
sudo named-checkconf
```

### 示例 2: 检查所有 zone

```bash
sudo named-checkconf -z
```

## 关联命令

- [[rndc|rndc]]
- [[dnsmasq|dnsmasq]]

## 风险提示

> ⚠️ **LOW**: 只读/信息查询类命令，风险较低，但仍需确认目标对象。

## 最佳实践

[[bp-named-checkconf|named-checkconf 生产环境最佳实践]]

## 所属维度

[[基础设施-MOC|网络工具/基础设施]]
