---
title: "trino-cli 生产环境最佳实践"
cmd_name: "trino-cli"
cmd_category: "大数据/调度与转换"
source_page: "[[trino-cli]]"
domain: "general"
risk_level: "medium"
platforms: ["linux", "darwin"]
tags: ["general", "risk-medium", "linux", "darwin"]
created: "2026-07-28"
source_file: "bigdata/orchestration.yaml"
---

# trino-cli — 生产环境最佳实践

> Trino (原 PrestoSQL) 分布式 SQL 查询引擎 CLI

| 属性 | 值 |
|------|------|
| 风险等级 | 🟡 中风险 |
| 领域 | `general` |
| 平台 | `linux`, `darwin` |
| 安装 | 下载 Trino CLI JAR 或 brew install trino (macOS) |

---

## 生产环境配置

- 关键系统命令变更（如 sysctl、systemctl）记录到变更管理系统
- 使用 Ansible/Salt 等配置管理工具统一管理系统参数
- 日志文件配置 logrotate 防止磁盘空间耗尽
- 定期执行安全更新，使用 `unattended-upgrades` 或等效工具自动化补丁

## 安全加固

- **MEDIUM**: 可跨数据源执行写操作（取决于 connector 配置）

## 性能调优

- 大数据量操作使用分批或流式处理，避免一次性加载
- 耗时命令考虑后台执行 + 进度通知机制

## 监控与告警

- 关键命令执行结果记录日志，异常时触发告警

## 常见反模式与避坑

- ❌ 在生产环境使用 `rm -rf` 等不可逆命令（应先移到临时目录确认后再删除）

## 高可用与灾备

- 关键操作使用幂等设计，故障恢复后可安全重试
- 配置文件和脚本纳入版本管理，支持快速恢复

## 生产示例

**交互式连接**:
```bash
trino --server localhost:8080 --catalog hive --schema default
```

## 参考链接

- (无外部参考)

## 关联命令最佳实践

- [[bp-clickhouse-client|clickhouse-client]]
- [[bp-spark-sql|spark-sql]]

---

## 运维 Checklist

- [ ] 命令风险等级：🟡 中风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 执行结果已记录到变更管理系统

---

[[trino-cli|命令详情]] | [[best-practices-MOC|最佳实践总索引]]
