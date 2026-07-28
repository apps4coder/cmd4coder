---
title: "k3d 生产环境最佳实践"
cmd_name: "k3d"
cmd_category: "容器编排/本地K8s"
source_page: "[[k3d]]"
domain: "container"
risk_level: "medium"
platforms: ["linux", "darwin", "windows"]
tags: ["container", "risk-medium", "linux", "darwin", "windows"]
created: "2026-07-28"
source_file: "container/k8s/local-k8s.yaml"
---

# k3d — 生产环境最佳实践

> 在 Docker 中运行 k3s 集群

| 属性 | 值 |
|------|------|
| 风险等级 | 🟡 中风险 |
| 领域 | `container` |
| 平台 | `linux`, `darwin`, `windows` |
| 安装 | 参考 https://k3d.io/v5.0.0/#installation |

---

## 生产环境配置

- 生产部署前在 staging 环境充分验证配置
- 使用 IaC 工具（Terraform/Pulumi）管理资源，避免手动操作

## 安全加固

- **MEDIUM**: 多个本地集群会占用大量资源，请及时清理不再使用的集群
- 禁止以 `--privileged` 模式运行容器
- 使用非 root 用户运行容器内进程 (`USER appuser`)

## 性能调优

- 大数据量操作使用分批或流式处理，避免一次性加载
- 耗时命令考虑后台执行 + 进度通知机制

## 监控与告警

- 集群指标通过 kube-state-metrics + node-exporter 采集
- 配置 Prometheus alerting rules：Pod 异常重启、节点 NotReady、PV 空间不足

## 常见反模式与避坑

- ❌ 手动 `kubectl edit` 修改生产资源（绕过 GitOps 审计链）
- ❌ 使用 `kubectl delete pod` 排查问题（破坏自愈机制，应先 drain）

## 高可用与灾备

- 关键工作负载至少 2 副本，跨可用区调度（`topologySpreadConstraints`）
- 配置 HPA 自动扩缩容应对流量波动

## 生产示例

**创建本地 k3s 集群**:
```bash
k3d cluster create mycluster
```
**导入本地镜像到 k3d 集群**:
```bash
k3d image import myapp:latest -c mycluster
```

## 参考链接

- (无外部参考)

## 关联命令最佳实践

- [[bp-kubectl|kubectl]]
- [[bp-kind|kind]]

---

## 运维 Checklist

- [ ] 命令风险等级：🟡 中风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 已确认备份/快照是最新的
- [ ] 已配置监控告警
- [ ] 执行结果已记录到变更管理系统

---

[[k3d|命令详情]] | [[best-practices-MOC|最佳实践总索引]]
