#!/usr/bin/env python3
"""AI 命令文档完整性校验（可作为 CI 检查）。

校验维度：
  1. YAML 必需字段：name/category/description/usage/examples/risks/platforms/
     related_commands/references，category 须属于 AI基础设施/*
  2. Markdown 生成完整性：根目录 <维度>/<slug>.md 与 <维度>/bp-<name>.md 存在，
     且 frontmatter 风险等级与 YAML 一致（取全部 risks 的最高级）
  3. 风险映射：bp 页属性表徽标、运维 Checklist 徽标与 YAML 风险等级一致；
     详情页风险提示章节包含全部 risks
  4. 链接关系：best-practices-MOC.md 收录全部 AI 命令且徽标正确、无悬空条目；
     详情页含指向 bp 页的最佳实践链接；related_commands 均指向真实命令

用法：python3 audit_ai_docs.py     （发现问题时退出码非 0）
"""
from __future__ import annotations

import glob
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
DATA_DIR = ROOT / "tools" / "cmd" / "data"
MOC_PATH = ROOT / "best-practices-MOC.md"

REQUIRED_FIELDS = [
    "name", "category", "description", "usage", "examples",
    "risks", "platforms", "related_commands", "references",
]
RISK_LEVELS = ["low", "medium", "high", "critical"]
RISK_BADGE = {
    "low": "🟢 低风险",
    "medium": "🟡 中风险",
    "high": "🟠 高风险",
    "critical": "🔴 严重风险",
}


def slugify(name: str) -> str:
    s = re.sub(r"[^\w\s-]", "", name)
    s = re.sub(r"[-\s]+", "-", s)
    return s.lower().strip("-")


def safe_filename(name: str) -> str:
    s = name.lower().strip()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff\-]", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "unknown"


def highest_risk(cmd: dict) -> str:
    worst = "low"
    for r in cmd.get("risks") or []:
        lvl = r.get("level", "low")
        if lvl in RISK_LEVELS and RISK_LEVELS.index(lvl) > RISK_LEVELS.index(worst):
            worst = lvl
    return worst


def load_commands():
    """返回 (AI 命令列表[(cmd, 维度, 源文件)], 全库命令名集合)。"""
    ai_cmds, all_names = [], set()
    for yf in sorted(glob.glob(str(DATA_DIR / "**" / "*.yaml"), recursive=True)):
        try:
            doc = yaml.safe_load(open(yf, encoding="utf-8"))
        except Exception as exc:
            print(f"⚠️ YAML 解析失败 {yf}: {exc}")
            continue
        if not isinstance(doc, dict):
            continue
        cat = str(doc.get("category") or "")
        for cmd in doc.get("commands") or []:
            name = cmd.get("name")
            if not name:
                continue
            all_names.add(name)
            if cat.startswith("AI基础设施"):
                ai_cmds.append((cmd, cat.split("/")[-1], Path(yf).relative_to(DATA_DIR).as_posix()))
    return ai_cmds, all_names


def frontmatter(text: str):
    """支持 JSON（详情页）与 YAML（bp 页）两种 frontmatter。"""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    raw = m.group(1)
    try:
        return json.loads(raw)
    except Exception:
        try:
            return yaml.safe_load(raw) or {}
        except Exception:
            return {}


def main() -> int:
    ai_cmds, all_names = load_commands()
    issues: list[str] = []
    add = issues.append

    moc_text = MOC_PATH.read_text(encoding="utf-8") if MOC_PATH.exists() else ""

    for cmd, dim, src in ai_cmds:
        name = cmd["name"]
        ctx = f"[{src}] {name}"

        # 1) YAML 必需字段
        for field in REQUIRED_FIELDS:
            if not cmd.get(field):
                add(f"{ctx}: YAML 缺少字段 {field}")
        if not str(cmd.get("category", "")).startswith("AI基础设施/"):
            add(f"{ctx}: 命令级 category 不属于 AI基础设施/*")

        # 4) related_commands 悬空
        for r in cmd.get("related_commands") or []:
            if r not in all_names:
                add(f"{ctx}: related_commands 悬空引用 '{r}'")

        worst = highest_risk(cmd)
        badge = RISK_BADGE[worst]

        # 2) 详情页
        detail = ROOT / dim / f"{slugify(name)}.md"
        if not detail.exists():
            add(f"{ctx}: 详情页缺失 {detail.relative_to(ROOT)}")
        else:
            text = detail.read_text(encoding="utf-8")
            fm = frontmatter(text)
            if fm.get("cmd_risk_level") != worst:
                add(f"{ctx}: 详情页 cmd_risk_level={fm.get('cmd_risk_level')} ≠ YAML 最高风险 {worst}")
            # 3) 风险章节包含全部 risks
            if cmd.get("risks"):
                if "## 风险提示" not in text:
                    add(f"{ctx}: 详情页缺少「风险提示」章节")
                else:
                    for r in cmd["risks"]:
                        lvl = r.get("level", "low").upper()
                        desc = r.get("description", "")
                        if desc and f"**{lvl}**: {desc}" not in text:
                            add(f"{ctx}: 详情页风险提示缺少 {lvl} 条目")
            # 4) 详情页 → bp 页链接
            if f"[[bp-{safe_filename(name)}|" not in text:
                add(f"{ctx}: 详情页缺少指向 bp 页的最佳实践链接")

        # 2) bp 页
        bp = ROOT / dim / f"bp-{safe_filename(name)}.md"
        if not bp.exists():
            add(f"{ctx}: 最佳实践页缺失 {bp.relative_to(ROOT)}")
        else:
            text = bp.read_text(encoding="utf-8")
            fm = frontmatter(text)
            if fm.get("risk_level") != worst:
                add(f"{ctx}: bp 页 risk_level={fm.get('risk_level')} ≠ YAML 最高风险 {worst}")
            if f"| 风险等级 | {badge} |" not in text:
                add(f"{ctx}: bp 页属性表风险徽标应为 {badge}")
            if f"命令风险等级：{badge}" not in text:
                add(f"{ctx}: bp 页 Checklist 风险徽标应为 {badge}")

        # 4) MOC 收录 + 徽标
        entry = f"[[bp-{safe_filename(name)}|{name}]]"
        if entry not in moc_text:
            add(f"{ctx}: best-practices-MOC.md 缺少条目 {entry}")
        elif f"{entry} {badge}" not in moc_text:
            add(f"{ctx}: MOC 条目徽标与 YAML 不符，应为 {badge}")

    # 4) MOC 悬空条目（AI 分类章节下链接的命令必须存在于 YAML）
    ai_names = {c["name"] for c, _, _ in ai_cmds}
    ai_bp_names = {f"bp-{safe_filename(n)}" for n in ai_names}
    section = None
    for line in moc_text.splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        if section and section.startswith("AI基础设施"):
            for m in re.finditer(r"\[\[(bp-[^\]|]+)\|", line):
                if m.group(1) not in ai_bp_names:
                    add(f"[MOC] {section} 悬空条目 {m.group(1)}")

    print(f"检查 AI 命令 {len(ai_cmds)} 个")
    if issues:
        print(f"❌ 发现 {len(issues)} 个问题：")
        for i in issues:
            print("  -", i)
        return 1
    print("✅ 全部通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
