---
{
  "cmd_name": "age",
  "cmd_category": "网络工具/安全扫描",
  "cmd_dimension": "安全扫描",
  "cmd_install": "brew install age (macOS) 或 apt install age (Ubuntu)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "sops",
    "gpg"
  ],
  "cmd_tags": [
    "safety",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/network/security-tools.yaml"
}
---

# age

> 现代文件加密工具（简单、安全、无配置）

## 安装

```bash
brew install age (macOS) 或 apt install age (Ubuntu)
```

## 用法

```
age [选项] [文件]
```

## 参数

| Flag | Description |
|------|-------------|
| `-e` | 加密 |
| `-d` | 解密 |
| `-r` | 指定接收者公钥 |
| `-i` | 指定身份文件（私钥） |
| `-o` | 输出文件 |

## 示例

### 示例 1: 生成密钥对

```bash
age-keygen -o key.txt
```

### 示例 2: 使用公钥加密文件

```bash
age -r age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p -o secret.age secret.txt
```

### 示例 3: 使用私钥解密文件

```bash
age -d -i key.txt -o secret.txt secret.age
```

### 示例 4: 加密压缩目录

```bash
tar czf - dir/ | age -r age1... -o backup.tar.gz.age
```

## 关联命令

- [[sops|sops]]

## 风险提示

> ⚠️ **HIGH**: 私钥丢失将导致加密数据永久不可恢复

## 最佳实践

[[bp-age|age 生产环境最佳实践]]

## 所属维度

[[安全扫描-MOC|网络工具/安全扫描]]
