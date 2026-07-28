---
title: "staticcheck 生产环境最佳实践"
cmd_name: "staticcheck"
cmd_category: "编程语言/Go工具链扩展"
source_page: "[[staticcheck]]"
domain: "devtool"
risk_level: "low"
platforms: ["linux", "darwin", "windows"]
tags: ["devtool", "risk-low", "linux", "darwin", "windows"]
created: "2026-07-28"
source_file: "lang/go-tooling.yaml"
---

# staticcheck — 生产环境最佳实践

> Go 高级静态分析工具（比 go vet 更深入）

| 属性 | 值 |
|------|------|
| 风险等级 | 🟢 低风险 |
| 领域 | `devtool` |
| 平台 | `linux`, `darwin`, `windows` |
| 安装 | go install honnef.co/go/tools/cmd/staticcheck@latest |

---

## 生产环境配置

- 关键系统命令变更（如 sysctl、systemctl）记录到变更管理系统
- 使用 Ansible/Salt 等配置管理工具统一管理系统参数
- 日志文件配置 logrotate 防止磁盘空间耗尽
- 定期执行安全更新，使用 `unattended-upgrades` 或等效工具自动化补丁

## 安全加固

- **LOW**: 只读检查操作，无风险

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

**检查所有包**:
```bash
staticcheck ./...
```

## 参考链接

- (无外部参考)

## 关联命令最佳实践

- [[bp-golangci-lint|golangci-lint]]
- [[bp-go-vet|go vet]]

---

## 运维 Checklist

- [ ] 命令风险等级：🟢 低风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 执行结果已记录到变更管理系统

---

[[staticcheck|命令详情]] | [[best-practices-MOC|最佳实践总索引]]
