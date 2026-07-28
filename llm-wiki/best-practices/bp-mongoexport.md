---
title: "mongoexport 生产环境最佳实践"
cmd_name: "mongoexport"
cmd_category: "数据库工具/NoSQL"
source_page: "[[mongoexport]]"
domain: "database"
risk_level: "medium"
platforms: ["linux", "darwin", "windows"]
tags: ["database", "risk-medium", "linux", "darwin", "windows"]
created: "2026-07-28"
source_file: "database/nosql.yaml"
---

# mongoexport — 生产环境最佳实践

> 将 MongoDB 集合导出为 JSON 或 CSV

| 属性 | 值 |
|------|------|
| 风险等级 | 🟡 中风险 |
| 领域 | `database` |
| 平台 | `linux`, `darwin`, `windows` |
| 安装 | 随 MongoDB Database Tools 安装 |

---

## 生产环境配置

- 生产数据库开启 TLS 加密传输
- 配置自动备份策略并定期验证恢复流程

## 安全加固

- **MEDIUM**: 导出的文件可能包含敏感信息，请妥善保管存储位置
- 数据库连接强制使用 TLS 加密
- 定期轮换数据库凭据，使用 Vault 动态 Secret

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

**导出集合为 JSON**:
```bash
mongoexport --uri="mongodb://localhost:27017/mydb" --collection users --out users.json
```

## 参考链接

- (无外部参考)

## 关联命令最佳实践

- [[bp-mongosh|mongosh]]
- [[bp-mongodump|mongodump]]

---

## 运维 Checklist

- [ ] 命令风险等级：🟡 中风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 已确认备份/快照是最新的
- [ ] 已配置监控告警
- [ ] 执行结果已记录到变更管理系统

---

[[mongoexport|命令详情]] | [[best-practices-MOC|最佳实践总索引]]
