---
{
  "cmd_name": "docker rmi",
  "cmd_category": "容器编排/Docker命令",
  "cmd_dimension": "Docker命令",
  "cmd_install": "参考 https://docs.docker.com/engine/install/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "docker images",
    "docker pull",
    "docker system prune"
  ],
  "cmd_tags": [
    "docker",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/container/docker/docker.yaml"
}
---

# docker rmi

> 删除本地镜像

## 安装

```bash
参考 https://docs.docker.com/engine/install/
```

## 用法

```
docker rmi [OPTIONS] IMAGE [IMAGE...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f, --force` | 强制删除镜像 |
| `--no-prune` | 不删除未标记的父镜像 |

## 示例

### 示例 1: 删除指定镜像

```bash
docker rmi nginx:latest
```

### 示例 2: 删除所有悬空镜像

```bash
docker rmi $(docker images -q -f dangling=true)
```

## 关联命令

- [[docker-images|docker images]]
- [[docker-pull|docker pull]]

## 风险提示

> ⚠️ **HIGH**: 会删除容器、镜像或网络资源，生产环境请确认对象并评估依赖影响。

## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
