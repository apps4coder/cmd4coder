---
{
  "cmd_name": "langchain",
  "cmd_category": "AI基础设施/Agent工程",
  "cmd_dimension": "Agent工程",
  "cmd_install": "pip install langchain",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "langgraph",
    "llama-index"
  ],
  "cmd_tags": [
    "agent",
    "application",
    "rag",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/agent-engineering.yaml"
}
---

# langchain

> LangChain LLM应用开发框架，支持Chains、Agents、RAG、工具调用

## 安装

```bash
pip install langchain
```

## 用法

```
python app.py (使用langchain库)
```

## 参数

| Flag | Description |
|------|-------------|
| `ChatOpenAI` | 聊天模型封装 |
| `create_react_agent` | 创建ReAct Agent |
| `RunnableParallel` | 并行执行多个Runnable |
| `Chroma` | 向量存储集成 |

## 示例

### 示例 1: 基础LLM调用

```bash
python -c "from langchain import OpenAI; llm = OpenAI(); print(llm.predict('hello'))"
```

### 示例 2: 构建RAG应用

```bash
python rag_app.py --model gpt-4 --vectorstore chroma --documents ./docs
```

### 示例 3: 多工具ReAct Agent

```bash
python agent.py --tools search,calculator --model claude-3
```

## 使用场景

- **RAG 应用**：拼接检索器、提示模板与 LLM 构建问答链。
- **工具调用 Agent**：通过 tool/function calling 编排多步推理。
- **多模型抽象**：统一封装不同提供商，便于切换与 A/B 实验。

## 生产环境最佳实践

- 复杂有环/有状态流程优先用 [[langgraph]]，LCEL 链适合无环管道。
- 用 LangSmith 做可观测（trace/token/延迟），生产环境必备。
- 用 `RunnableWithMessageHistory` 管理会话，避免把历史全量塞入提示导致超窗口。
- 为外部调用设超时与重试，避免单点阻塞整个链。
- 锁定依赖版本（langchain-core / 各 integration 包独立演进，易破坏兼容）。

## 故障排除

| 现象 | 可能原因 | 处理 |
|------|----------|------|
| ImportError/类不存在 | 版本分包后路径变化 | 改从 `langchain_openai` 等独立包导入，对齐版本 |
| 上下文超长报错 | 历史/文档过长 | 加入截断、摘要或分段检索 |
| 工具不被调用 | 模型不支持/描述不清 | 换支持 function calling 的模型，优化工具 docstring |
| 成本失控 | 没有限制调用 | 用 LangSmith 监控 token，设 max_iterations |

## 关联与依赖

- **图式编排**：[[langgraph]] 是官方有状态/循环 Agent 方案。
- **替代框架**：[[llama-index]]（偏检索）、[[crewai]]（多 Agent 协作）。
- **后端依赖**：可接 [[ollama]]/[[vllm]] 本地模型或 [[openrouter]] 网关。

## 安全与风险注意事项

- Agent 可能执行任意工具（包括 shell/代码执行），需白名单工具并沙箱隔离。
- 提示注入可能诱导 Agent 调用敏感工具，需对工具输入做校验与权限控制。

## 关联命令

- [[langgraph]]
- [[llama-index]]

## 风险提示

> ⚠️ **MEDIUM**: Agent可能执行不可预期操作，需限制工具权限

## 参考链接

- [https://python.langchain.com/](https://python.langchain.com/)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
