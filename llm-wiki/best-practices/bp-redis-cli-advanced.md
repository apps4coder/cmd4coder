---
title: "redis-cli (advanced) 生产环境最佳实践"
cmd_name: "redis-cli (advanced)"
cmd_category: "数据库工具/运维操作"
source_page: "[[redis-cli-advanced]]"
domain: "database"
risk_level: "high"
platforms: ["linux", "darwin"]
tags: ["database", "risk-high", "linux", "darwin"]
created: "2026-07-28"
source_file: "database/operations.yaml"
---

# redis-cli (advanced) — 生产环境最佳实践

> Redis 高级运维操作（集群、持久化、内存分析）

| 属性 | 值 |
|------|------|
| 风险等级 | 🟠 高风险 |
| 领域 | `database` |
| 平台 | `linux`, `darwin` |
| 安装 | 随 Redis 安装 |

---

## 生产环境配置

- 生产环境设置 `maxmemory` + `maxmemory-policy` 防止 OOM
- 启用 `requirepass` 或 ACL 认证，禁止无密码暴露
- 使用 Sentinel 或 Cluster 模式保障高可用
- 配置 `tcp-backlog` 和 `timeout` 参数适配高并发场景

## 安全加固

- ⚠️ 此命令风险等级为 **HIGH**，生产环境使用前必须经过变更审批
- **HIGH**: reshard 影响集群数据分布，FLUSHALL 清空所有数据
- 数据库连接强制使用 TLS 加密
- 定期轮换数据库凭据，使用 Vault 动态 Secret
- 操作前务必在 staging 环境验证，制定回滚方案

## 性能调优

- 连接池配置：最小连接数 ≥ 应用实例数，最大连接数根据数据库 max_connections 合理设置
- 大表操作（ALTER、DELETE）使用分批执行或在线 DDL 工具

## 监控与告警

- 监控连接数、慢查询数、复制延迟、磁盘使用率
- 配置告警：连接池耗尽、主从延迟 > 5s、磁盘使用率 > 80%

## 常见反模式与避坑

- ❌ 在生产库直接执行未经审核的 DDL（应走 schema migration 流程）
- ❌ 使用 root/superuser 连接应用（应创建最小权限的应用专用账号）
- ❌ 关闭 binlog/WAL 提升性能（牺牲恢复能力）

## 高可用与灾备

- 配置自动故障转移（RDS Multi-AZ / Patroni / Redis Sentinel）
- 定期执行备份恢复演练，验证 RTO/RPO 是否满足 SLA
- 备份存储跨区域复制，防止区域级故障

## 生产示例

**检查集群健康状态**:
```bash
redis-cli --cluster check 127.0.0.1:7000
```

## 参考链接

- (无外部参考)

## 关联命令最佳实践

- [[bp-redis-server|redis-server]]
- [[bp-redis-sentinel|redis-sentinel]]

---

## 运维 Checklist

- [ ] 命令风险等级：🟠 高风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 已获得变更审批
- [ ] 已制定回滚方案
- [ ] 已通知相关 oncall 人员
- [ ] 已确认备份/快照是最新的
- [ ] 已配置监控告警
- [ ] 执行结果已记录到变更管理系统

---

[[redis-cli-advanced|命令详情]] | [[best-practices-MOC|最佳实践总索引]]
