---
title: "efibootmgr 生产环境最佳实践"
cmd_name: "efibootmgr"
cmd_category: "硬件/固件与UEFI"
source_page: "[[efibootmgr]]"
domain: "general"
risk_level: "critical"
platforms: ["linux", "darwin"]
tags: ["general", "risk-critical", "linux", "darwin"]
created: "2026-07-28"
source_file: "hardware/firmware.yaml"
---

# efibootmgr — 生产环境最佳实践

> 管理 UEFI 启动项

| 属性 | 值 |
|------|------|
| 风险等级 | 🔴 严重风险 |
| 领域 | `general` |
| 平台 | `linux`, `darwin` |
| 安装 | 多数 Linux 预装或 efibootmgr 包 |

---

## 生产环境配置

- 关键系统命令变更（如 sysctl、systemctl）记录到变更管理系统
- 使用 Ansible/Salt 等配置管理工具统一管理系统参数
- 日志文件配置 logrotate 防止磁盘空间耗尽
- 定期执行安全更新，使用 `unattended-upgrades` 或等效工具自动化补丁

## 安全加固

- ⚠️ 此命令风险等级为 **CRITICAL**，生产环境使用前必须经过变更审批
- **CRITICAL**: 删除或修改错误的启动项会导致系统无法启动
- **CRITICAL**: 操作前请仔细阅读文档并确认参数，建议在测试环境或非生产数据上先行验证。
- 操作前务必在 staging 环境验证，制定回滚方案

## 性能调优

- 大数据量操作使用分批或流式处理，避免一次性加载
- 耗时命令考虑后台执行 + 进度通知机制

## 监控与告警

- 关键命令执行结果记录日志，异常时触发告警

## 常见反模式与避坑

- ❌ 在生产环境使用 `rm -rf` 等不可逆命令（应先移到临时目录确认后再删除）
- ❌ 未经审批直接执行高风险操作

## 高可用与灾备

- 关键操作使用幂等设计，故障恢复后可安全重试
- 配置文件和脚本纳入版本管理，支持快速恢复

## 生产示例

**列出启动项**:
```bash
efibootmgr -v
```

## 参考链接

- (无外部参考)

## 关联命令最佳实践

- [[bp-efivar|efivar]]
- grub-install

---

## 运维 Checklist

- [ ] 命令风险等级：🔴 严重风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 已获得变更审批
- [ ] 已制定回滚方案
- [ ] 已通知相关 oncall 人员
- [ ] 执行结果已记录到变更管理系统

---

[[efibootmgr|命令详情]] | [[best-practices-MOC|最佳实践总索引]]
