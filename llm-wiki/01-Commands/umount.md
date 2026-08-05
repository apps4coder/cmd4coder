---
{
  "cmd_name": "umount",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "mount",
    "lsof"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/os/linux-extra.yaml"
}
---

# umount

> 卸载文件系统

## 用法

```
umount [OPTIONS] TARGET
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | 懒卸载 |
| `-f` | 强制卸载 |
| `-r` | 失败时以只读重新挂载 |

## 示例

### 示例 1: 卸载 /mnt

```bash
sudo umount /mnt
```

### 示例 2: 懒卸载（允许进程退出后完全释放）

```bash
sudo umount -l /mnt
```

## 关联命令

- [[mount|mount]]
- [[lsof|lsof]]

## 风险提示

> ⚠️ **HIGH**: 卸载时若有进程占用会导致失败或数据不一致，请先确认无活跃访问

> ⚠️ **HIGH**: 操作前请仔细阅读文档并确认参数，建议在测试环境或非生产数据上先行验证。

## 最佳实践

[[bp-umount|umount 生产环境最佳实践]]

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
