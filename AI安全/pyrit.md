---
{
  "cmd_name": "pyrit",
  "cmd_category": "AI基础设施/AI安全",
  "cmd_dimension": "AI安全",
  "cmd_install": "pip install pyrit",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "garak",
    "rebuff"
  ],
  "cmd_tags": [
    "safety",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/ai-safety.yaml"
}
---

# pyrit

> PyRIT (微软开源) 生成式AI红队自动化框架，编排多轮攻击、评分与风险证据收集

## 安装

```bash
pip install pyrit
```

## 用法

```
python redteam.py (使用pyrit库)
```

## 参数

| Flag | Description |
|------|-------------|
| `PromptSendingOrchestrator` | 批量发送攻击prompt的编排器 |
| `RedTeamingOrchestrator` | 多轮自适应红队对话 |
| `SelfAskTrueFalseScorer` | 基于LLM的攻击成功与否评分器 |

## 示例

### 示例 1: 启动多轮自适应红队攻击目标模型

```bash
python -c "from pyrit.orchestrator import RedTeamingOrchestrator; ..."
```

### 示例 2: 批量发送攻击prompt并收集结果

```bash
python -c "from pyrit.orchestrator import PromptSendingOrchestrator; orch.send_prompts_async(prompts)"
```

## 关联命令

- [[garak|garak]]
- [[rebuff|rebuff]]

## 风险提示

> ⚠️ **HIGH**: 生成真实攻击载荷，仅限授权红队测试，禁止用于未授权系统

> ⚠️ **MEDIUM**: 攻击编排器会调用目标LLM API产生费用，大规模红队测试前应设置速率与调用上限

## 参考链接

- [https://github.com/Azure/PyRIT](https://github.com/Azure/PyRIT)

## 最佳实践

[[bp-pyrit|pyrit 生产环境最佳实践]]

## 所属维度

[[AI安全-MOC|AI基础设施/AI安全]]
