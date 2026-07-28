---
title: "flux 生产环境最佳实践"
cmd_name: "flux"
cmd_category: "CI-CD/GitOps"
source_page: "[[flux]]"
domain: "cicd"
risk_level: "medium"
platforms: ["linux", "darwin"]
tags: ["cicd", "risk-medium", "linux", "darwin"]
created: "2026-07-28"
source_file: "cicd/gitops.yaml"
---

# flux — 生产环境最佳实践

> Flux CD CLI，云原生 GitOps 持续交付工具

| 属性 | 值 |
|------|------|
| 风险等级 | 🟡 中风险 |
| 领域 | `cicd` |
| 平台 | `linux`, `darwin` |
| 安装 | brew install fluxcd/tap/flux (macOS) 或 curl -s https://fluxcd.io/install.sh | bash |

---

## 生产环境配置

- 生产部署流水线必须包含自动化测试、安全扫描和审批步骤
- Secrets 使用 Vault/SSM 管理，禁止明文存储在配置文件中
- 构建镜像使用固定 digest 而非 `latest` 标签
- 配置流水线超时和并发限制，防止资源争抢

## 安全加固

- **MEDIUM**: 操作影响集群中的 GitOps 流水线

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

**在集群中安装 Flux**:
```bash
flux install
```

## 参考链接

- (无外部参考)

## 关联命令最佳实践

- flux create
- [[bp-flux-reconcile|flux reconcile]]
- [[bp-kubectl|kubectl]]

---

## 运维 Checklist

- [ ] 命令风险等级：🟡 中风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 执行结果已记录到变更管理系统

---

[[flux|命令详情]] | [[best-practices-MOC|最佳实践总索引]]
