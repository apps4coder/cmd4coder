---
{
  "cmd_name": "interpretml",
  "cmd_category": "AI基础设施/模型可解释性",
  "cmd_dimension": "模型可解释性",
  "cmd_install": "pip install interpret",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "shap",
    "lime"
  ],
  "cmd_tags": [
    "interpretability",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/model-interpretability.yaml"
}
---

# interpretml

> InterpretML (微软开源) 统一可解释性工具包，提供玻璃盒模型(EBM)与黑盒模型事后解释

## 安装

```bash
pip install interpret
```

## 用法

```
python explain.py (使用interpret库)
```

## 参数

| Flag | Description |
|------|-------------|
| `ExplainableBoostingClassifier` | 可解释提升机玻璃盒模型 |
| `show` | 启动交互式解释仪表板 |
| `explain_global` | 全局特征重要性解释 |
| `explain_local` | 单样本局部解释 |

## 示例

### 示例 1: 训练可解释EBM玻璃盒模型

```bash
python -c "from interpret.glassbox import ExplainableBoostingClassifier; ebm = ExplainableBoostingClassifier().fit(X, y)"
```

### 示例 2: 启动交互式全局解释仪表板

```bash
python -c "from interpret import show; show(ebm.explain_global())"
```

## 关联命令

- [[shap|shap]]
- [[lime|lime]]

## 风险提示

> ⚠️ **LOW**: 可视化仪表板默认监听本地端口，生产环境避免暴露

## 参考链接

- [https://interpret.ml/](https://interpret.ml/)

## 最佳实践

[[bp-interpretml|interpretml 生产环境最佳实践]]

## 所属维度

[[模型可解释性-MOC|AI基础设施/模型可解释性]]
