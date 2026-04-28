"""physique-girls-navi 自動記事生成エントリ"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, r"C:\Users\atsus\000_ClaudeCode\007_自動投稿ブログ")
import fitness_auto_post_lib as lib  # noqa: E402

CLAUDE_MD = (HERE / "CLAUDE.md").read_text(encoding="utf-8") if (HERE / "CLAUDE.md").exists() else ""

CFG = {
    "site_dir": HERE,
    "blog_name": "フィジーク女子ナビ",
    "site_url": "https://musclelove-777.github.io/physique-girls-navi",
    "twitter_site": "@MuscleGirlLove7",
    "accent_color": "#9c27b0",
    "categories": [
        "選手紹介", "大会・コンテスト情報", "ポージング・コンテスト準備",
        "減量・コンディショニング", "トレーニング", "コラム",
    ],
    "seed_topics": CLAUDE_MD,
    "image_query": "physique women bodybuilding",
}

if __name__ == "__main__":
    res = lib.run(CFG)
    print(res)
