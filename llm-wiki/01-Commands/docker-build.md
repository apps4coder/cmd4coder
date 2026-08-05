---
{
  "cmd_name": "docker build",
  "cmd_category": "容器编排/Docker命令",
  "cmd_dimension": "Docker命令",
  "cmd_install": "参考 https://docs.docker.com/engine/install/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "docker run",
    "docker push"
  ],
  "cmd_tags": [
    "docker",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/container/docker/docker.yaml"
}
---

# docker build

> 从Dockerfile构建镜像

## 安装

```bash
参考 https://docs.docker.com/engine/install/
```

## 用法

```
docker build [OPTIONS] PATH
```

## 参数

| Flag | Description |
|------|-------------|
| `-t, --tag` | 镜像名称和标签 |
| `-f, --file` | 指定Dockerfile路径 |
| `--no-cache` | 不使用缓存 |

## 示例

### 示例 1: 构建镜像并打标签

```bash
docker build -t myapp:1.0 .
```

### 示例 2: 不使用缓存构建

```bash
docker build --no-cache -t myapp .
```

## 关联命令

- [[docker-run|docker run]]
- [[docker-push|docker push]]

## 风险提示

> ⚠️ **MEDIUM**: 会改变容器生命周期或构建新镜像，请在测试环境验证参数后再用于生产。

## 最佳实践

[[bp-docker-build|docker build 生产环境最佳实践]]

## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
