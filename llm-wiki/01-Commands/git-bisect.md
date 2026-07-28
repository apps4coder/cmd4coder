---
{
  "cmd_name": "git bisect",
  "cmd_category": "版本控制/Git高级操作",
  "cmd_dimension": "Git高级操作",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "git log",
    "git blame"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/vcs/git-advanced.yaml"
}
---

# git bisect

> 二分查找定位引入 bug 的提交

## 用法

```
git bisect start
```

```
git bisect good [提交]
```

```
git bisect bad [提交]
```

## 参数

| Flag | Description |
|------|-------------|
| `start` | 开始二分查找 |
| `good` | 标记正常提交 |
| `bad` | 标记异常提交 |
| `reset` | 结束并重置 |
| `run` | 自动化测试脚本 |

## 示例

### 示例 1: 在 v1.0.0 和 HEAD 间二分

```bash
git bisect start && git bisect bad HEAD && git bisect good v1.0.0
```

### 示例 2: 自动化二分（脚本退出码判断好坏）

```bash
git bisect run ./test.sh
```

### 示例 3: 结束二分查找

```bash
git bisect reset
```

## 关联命令

- [[git-log|git log]]

## 风险提示

> ⚠️ **LOW**: 只读操作，reset 恢复正常状态

## 所属维度

[[Git高级操作-MOC|版本控制/Git高级操作]]
