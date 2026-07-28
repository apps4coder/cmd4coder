---
{
  "cmd_name": "langgraph",
  "cmd_category": "AI基础设施/Agent工程",
  "cmd_dimension": "Agent工程",
  "cmd_install": "pip install langgraph",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "langchain",
    "crewai"
  ],
  "cmd_tags": [
    "agent",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/agent-engineering.yaml"
}
---

# langgraph

> LangGraph状态机Agent框架，支持循环、条件分支、持久化、人机协同

## 安装

```bash
pip install langgraph
```

## 用法

```
python app.py (使用langgraph库)
```

## 参数

| Flag | Description |
|------|-------------|
| `StateGraph` | 定义状态图 |
| `add_node` | 添加节点 |
| `add_edge` | 添加边 |
| `compile` | 编译为可运行应用 |

## 示例

### 示例 1: 定义简单Agent状态图

```bash
python -c "from langgraph.graph import StateGraph; builder = StateGraph(State); builder.add_node('agent', call_model); builder.add_edge('agent', END); graph = builder.compile()"
```

### 示例 2: 带检查点和人机协同的Agent

```bash
python agent_loop.py --checkpoint --interrupt human_approval
```

## 使用场景

- **有状态多步 Agent**：需要循环、条件分支、重试的复杂工作流。
- **人机协同（HITL）**：在关键步骤中断等待人工审批。
- **多 Agent 编排**：多个角色节点协作完成任务。

## 生产环境最佳实践

- 用 checkpointer（如 `PostgresSaver`/`SqliteSaver`）持久化状态，支持断点续跑与回溯。
- 为每个图设 `recursion_limit`，防止循环失控。
- 用 `interrupt` 实现 HITL，将审批点显式建模，而非靠提示约束。
- 节点保持幂等与无副作用，便于重放与测试。
- 用 `thread_id` 隔离不同会话的状态。

## 故障排除

| 现象 | 可能原因 | 处理 |
|------|----------|------|
| GraphRecursionError | 陷入循环 | 调优路由条件，适当提高 `recursion_limit` 并加终止判断 |
| 状态丢失 | 未配 checkpointer | 配置持久化 saver 并传入 `thread_id` |
| 状态字段被覆盖 | 未定义 reducer | 用 `Annotated[list, add]` 等 reducer 合并更新 |
| 中断后无法恢复 | 未传相同 thread | 恢复时传入相同 `configurable.thread_id` |

## 关联与依赖

- **建在**：[[langchain]] 生态之上，可直接复用其 LLM/工具抽象。
- **替代/互补**：[[crewai]]（角色化多 Agent）、[[autogen]]。
- **持久化依赖**：Postgres/SQLite/Redis 作为 checkpointer 后端。

## 安全与风险注意事项

- 循环 Agent 可能无限迭代消耗 token/费用，必须设迭代上限与预算报警。
- 持久化状态可能含敏感上下文，checkpointer 存储需加密与访问控制。

## 关联命令

- [[langchain]]
- [[crewai]]

## 风险提示

> ⚠️ **MEDIUM**: 循环Agent可能陷入无限循环，需设置最大迭代

## 参考链接

- [https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
