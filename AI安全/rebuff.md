---
{
  "cmd_name": "rebuff",
  "cmd_category": "AI基础设施/AI安全",
  "cmd_dimension": "AI安全",
  "cmd_install": "pip install rebuff",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "llm-guard",
    "garak"
  ],
  "cmd_tags": [
    "safety",
    "vector-db",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "tools/cmd/data/ai/ai-safety.yaml"
}
---

# rebuff

> Rebuff 提示注入检测库，多层防御（启发式+LLM+向量库+金丝雀）拦截恶意prompt

## 安装

```bash
pip install rebuff
```

## 用法

```
python guard.py (使用rebuff库)
```

## 参数

| Flag | Description |
|------|-------------|
| `detect_injection` | 检测输入是否包含注入攻击 |
| `add_canary_word` | 注入金丝雀词检测提示泄露 |

## 示例

### 示例 1: 检测典型越狱提示

```bash
python -c "from rebuff import Rebuff; rb = Rebuff(api_token='...'); result = rb.detect_injection('ignore previous instructions')"
```

### 示例 2: 使用金丝雀词机制检测提示泄露

```bash
python -c "from rebuff import Rebuff; rb = Rebuff(api_token='...'); buffed = rb.add_canary_word(prompt); # 在输出中检测金丝雀词是否泄露"
```

## 关联命令

- [[llm-guard|llm-guard]]
- [[garak|garak]]

## 风险提示

> ⚠️ **LOW**: 检测为概率性，不能作为唯一防线，需与输出过滤配合

## 参考链接

- [https://github.com/protectai/rebuff](https://github.com/protectai/rebuff)

## 所属维度

[[AI安全-MOC|AI基础设施/AI安全]]
