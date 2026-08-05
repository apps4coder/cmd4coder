---
{
  "cmd_name": "docker build (multi-stage)",
  "cmd_category": "容器编排/Docker高级",
  "cmd_dimension": "Docker高级",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "docker buildx",
    "docker compose"
  ],
  "cmd_tags": [
    "docker",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/container/docker/docker-advanced.yaml"
}
---

# docker build (multi-stage)

> Docker 多阶段构建（减小镜像体积）

## 用法

```
docker build [选项] [路径]
```

## 参数

| Flag | Description |
|------|-------------|
| `--target` | 构建到指定阶段 |
| `--build-arg` | 构建参数 |
| `--no-cache` | 不使用缓存 |
| `-t` | 镜像标签 |
| `--secret` | 构建时密钥（不留在镜像中） |

## 示例

### 示例 1: 构建到 production 阶段

```bash
docker build --target production -t myapp:v1 .
```

### 示例 2: 传入构建参数

```bash
docker build --build-arg VERSION=1.9.0 -t myapp:v1 .
```

### 示例 3: 使用构建密钥（不泄露到镜像）

```bash
docker build --secret id=npm_token,src=.npmrc -t myapp:v1 .
```

### 示例 4: 无缓存全新构建

```bash
docker build --no-cache --pull -t myapp:v1 .
```

## 关联命令

- [[docker-buildx|docker buildx]]
- [[docker-compose|docker compose]]

## 风险提示

> ⚠️ **LOW**: 构建操作风险低

## 最佳实践

[[bp-docker-build-multi-stage|docker build (multi-stage) 生产环境最佳实践]]

## 所属维度

[[Docker高级-MOC|容器编排/Docker高级]]
