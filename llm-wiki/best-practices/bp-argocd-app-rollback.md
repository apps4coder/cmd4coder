---
title: "argocd app rollback 生产环境最佳实践"
cmd_name: "argocd app rollback"
cmd_category: "CI-CD/GitOps"
source_page: "[[argocd-app-rollback]]"
domain: "cicd"
risk_level: "high"
platforms: ["linux", "darwin"]
tags: ["cicd", "risk-high", "linux", "darwin"]
created: "2026-07-28"
source_file: "cicd/gitops.yaml"
---

# argocd app rollback — 生产环境最佳实践

> 回滚 ArgoCD 应用到历史版本

| 属性 | 值 |
|------|------|
| 风险等级 | 🟠 高风险 |
| 领域 | `cicd` |
| 平台 | `linux`, `darwin` |
| 安装 | 同 argocd |

---

## 生产环境配置

- 生产部署流水线必须包含自动化测试、安全扫描和审批步骤
- Secrets 使用 Vault/SSM 管理，禁止明文存储在配置文件中
- 构建镜像使用固定 digest 而非 `latest` 标签
- 配置流水线超时和并发限制，防止资源争抢

## 安全加固

- ⚠️ 此命令风险等级为 **HIGH**，生产环境使用前必须经过变更审批
- **HIGH**: 回滚影响生产部署，确认目标修订正确
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

**查看应用部署历史**:
```bash
argocd app history my-app
```

## 参考链接

- (无外部参考)

## 关联命令最佳实践

- [[bp-argocd-app-sync|argocd app sync]]
- argocd app history

---

## 运维 Checklist

- [ ] 命令风险等级：🟠 高风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 已获得变更审批
- [ ] 已制定回滚方案
- [ ] 已通知相关 oncall 人员
- [ ] 执行结果已记录到变更管理系统

---

[[argocd-app-rollback|命令详情]] | [[best-practices-MOC|最佳实践总索引]]
