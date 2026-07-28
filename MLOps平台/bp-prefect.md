---
title: "prefect 生产环境最佳实践"
cmd_name: "prefect"
cmd_category: "AI基础设施/MLOps平台"
source_page: "[[prefect]]"
domain: "ai-infra"
risk_level: "low"
platforms: ["linux", "darwin", "windows"]
tags: ["ai-infra", "risk-low", "linux", "darwin", "windows"]
created: "2026-07-28"
source_file: "ai/mlops.yaml"
---

# prefect — 生产环境最佳实践

> Prefect 现代化工作流编排CLI，Python原生Flow定义，支持动态DAG与混合执行

| 属性 | 值 |
|------|------|
| 风险等级 | 🟢 低风险 |
| 领域 | `ai-infra` |
| 平台 | `linux`, `darwin`, `windows` |
| 安装 | pip install prefect |

---

## 生产环境配置

- GPU 工作负载使用 node selector/taint 调度到专用节点池
- 配置 GPU 监控 (nvidia-smi → Prometheus exporter)

## 安全加固

- **LOW**: Cloud模式下Flow元数据上传至SaaS，需评估数据合规
- 模型服务 API 接入认证（JWT/API Key），禁止匿名访问
- 输入数据做长度和格式校验，防止 Prompt 注入

## 性能调优

- GPU 工作负载配置 GPU 分时复用或 MIG 切分

## 监控与告警

- GPU 监控：利用率、显存、温度、ECC 错误（通过 DCGM exporter）

## 常见反模式与避坑

- ❌ 推理服务不设置超时（长请求占用 GPU 资源导致后续请求排队）
- ❌ 训练任务不保存 checkpoint（spot 实例抢占导致训练丢失）
- ❌ 模型服务直接暴露公网（应前置 API Gateway + 认证）

## 高可用与灾备

- 推理服务部署多副本 + 负载均衡，单点故障自动摘除
- 模型文件存储在共享存储（S3/NFS），多副本可独立加载
- 训练 checkpoint 定期上传到持久化存储，支持断点续训

## 生产示例

**将训练Flow部署到gpu-pool工作池**:
```bash
prefect deploy ./train.py:train_flow -n nightly-train -p gpu-pool
```
**手动触发一次部署运行**:
```bash
prefect deployment run 'train-flow/nightly-train'
```

## 参考链接

- [https://docs.prefect.io/latest/api-ref/cli/](https://docs.prefect.io/latest/api-ref/cli/)

## 关联命令最佳实践

- [[bp-airflow|airflow]]
- [[bp-dagster|dagster]]
- [[bp-metaflow|metaflow]]

---

## 运维 Checklist

- [ ] 命令风险等级：🟢 低风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 已确认备份/快照是最新的
- [ ] 已配置监控告警
- [ ] 执行结果已记录到变更管理系统

---

[[prefect|命令详情]] | [[best-practices-MOC|最佳实践总索引]]
