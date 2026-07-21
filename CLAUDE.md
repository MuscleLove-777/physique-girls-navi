# フィジーク女子ナビ - リモートエージェントガイド

## プロジェクト概要
「フィジーク女子ナビ」はビキニフィットネス・フィジーク・ボディビルで活躍する女子選手の最新情報を毎日発信するGitHub Pagesファンサイトです。

- 運営: MuscleLove
- URL: https://musclelove-777.github.io/physique-girls-navi/
- X: @MuscleGirlLove7
- Patreon: https://www.patreon.com/MuscleLove

## 掲載対象（ロスター）
記事対象の選手リストは必ず `references/roster.md` を読んで参照すること。リストの追加・更新もそのファイルに対して行う。

## 記事生成ルール

1. **言語**: 日本語
2. **文字数**: 200〜400文字（本文）
3. **トーン**: キャッチーでファン目線。選手への敬意を忘れず、ワクワク感のある文章
4. **内容の種類**:
   - 大会結果速報
   - 選手のSNS情報・トレーニング情報
   - 大会プレビュー・見どころ
   - トレーニングTips
   - 選手紹介・プロフィール
5. **ヒーロー画像**: 各記事にUnsplash画像を1枚使用
   - フィットネス・ジム・トレーニング関連の画像を使う
   - 形式: `https://images.unsplash.com/photo-XXXXX?w=1200&h=400&fit=crop`
6. **WebSearchで最新情報を必ず検索してから記事を書く**
   - 検索キーワード例: 「ビキニフィットネス 2026」「JBBF 大会 結果」「FWJ 2026」「フィジーク 女子 ニュース」
7. **事実確認**: 検索結果に基づいた正確な情報のみ記載。不確かな情報は書かない

## ファイル構成

```
physique-girls-navi/
├── index.html          # トップページ（選手カード + ブログ一覧）
├── CLAUDE.md           # このファイル
├── sitemap.xml         # サイトマップ
├── robots.txt          # robots.txt
└── articles/           # 記事ディレクトリ
    ├── 2026-04-04-jbbf-2026-schedule.html
    ├── 2026-04-04-yasui-yuri-season.html
    └── 2026-04-04-fwj-2026-season-open.html
```

## 記事HTMLテンプレート

新しい記事は以下のテンプレートで作成:

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【記事タイトル】 | フィジーク女子ナビ</title>
  <meta name="description" content="記事の説明文（120文字以内）">
  <meta property="og:title" content="記事タイトル">
  <meta property="og:description" content="記事の説明文">
  <meta property="og:image" content="https://images.unsplash.com/photo-XXXXX?w=1200&h=630&fit=crop">
  <meta property="og:type" content="article">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@MuscleGirlLove7">
  <link rel="canonical" href="https://musclelove-777.github.io/physique-girls-navi/articles/ファイル名.html">
  <style>
    *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
    :root { --bg: #0d1117; --bg-card: #161b22; --accent: #e91e63; --accent-light: #f06292; --text: #e6edf3; --text-muted: #8b949e; --border: #30363d; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans JP', sans-serif; background: var(--bg); color: var(--text); line-height: 1.8; }
    a { color: var(--accent-light); text-decoration: none; }
    a:hover { color: var(--accent); }
    .header { background: var(--bg-card); border-bottom: 1px solid var(--border); padding: 14px 20px; }
    .header-inner { max-width: 800px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }
    .logo { font-size: 1.1rem; font-weight: 700; color: var(--accent); }
    .hero-img { width: 100%; max-height: 400px; object-fit: cover; }
    .article { max-width: 800px; margin: 0 auto; padding: 40px 20px; }
    .article .date { color: var(--text-muted); font-size: 0.85rem; margin-bottom: 12px; }
    .article h1 { font-size: 1.8rem; font-weight: 800; margin-bottom: 20px; line-height: 1.4; }
    .article p { margin-bottom: 16px; color: var(--text); font-size: 1rem; }
    .article h2 { font-size: 1.3rem; margin: 30px 0 12px; padding-left: 12px; border-left: 4px solid var(--accent); }
    .article ul { margin: 0 0 16px 20px; }
    .article li { margin-bottom: 6px; color: var(--text-muted); }
    .back-link { display: inline-block; margin-top: 30px; padding: 10px 24px; background: var(--accent); color: #fff; border-radius: 8px; font-weight: 600; }
    .back-link:hover { background: var(--accent-light); color: #fff; }
    .footer { border-top: 1px solid var(--border); padding: 30px 20px; text-align: center; color: var(--text-muted); font-size: 0.85rem; margin-top: 40px; }
  </style>
</head>
<body>

<header class="header">
  <div class="header-inner">
    <a href="../index.html" class="logo">フィジーク女子ナビ</a>
    <a href="../index.html">トップへ戻る</a>
  </div>
</header>

<img class="hero-img" src="https://images.unsplash.com/photo-XXXXX?w=1200&h=400&fit=crop" alt="記事タイトル">

<article class="article">
  <div class="date">YYYY年M月D日</div>
  <h1>記事タイトル</h1>

  <!-- 本文をここに書く（200〜400文字） -->

  <a href="../index.html" class="back-link">&larr; トップページへ</a>
</article>

<!-- ML_PROMO_CARD_START -->
<section style="max-width:800px;margin:32px auto;padding:0 20px;">
  <div style="background:#111827;border:1px solid rgba(255,255,255,0.14);border-radius:10px;padding:24px;text-align:center;">
    <p style="margin:0 0 6px;color:#f0f0f5;font-weight:800;">MuscleLove 公式</p>
    <p style="margin:0 0 14px;color:#9ca3af;font-size:0.9rem;">最新情報・限定コンテンツはこちら</p>
    <div style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center;">
      <a href="https://x.com/MuscleGirlLove7" target="_blank" rel="noopener" style="display:inline-block;padding:10px 18px;background:#1d9bf0;color:#fff;border-radius:6px;font-weight:800;text-decoration:none;">X @MuscleGirlLove7</a>
      <a href="https://www.patreon.com/MuscleLove" target="_blank" rel="noopener" style="display:inline-block;padding:10px 18px;background:#ff424d;color:#fff;border-radius:6px;font-weight:800;text-decoration:none;">Patreon 限定コンテンツ</a>
      <a href="https://musclelove-games.vercel.app/?utm_source=blog&amp;utm_medium=promo_card&amp;utm_campaign=physique-girls-navi" target="_blank" rel="noopener" style="display:inline-block;padding:10px 18px;background:#22c55e;color:#0b1220;border-radius:6px;font-weight:800;text-decoration:none;">🎮 無料ブラウザゲームで遊ぶ</a>
    </div>
  </div>
</section>
<!-- ML_PROMO_CARD_END -->

<footer class="footer">
  &copy; 2026 MuscleLove - フィジーク女子ナビ
</footer>

</body>
</html>
```

## index.html更新方法

新しい記事を追加したら、index.htmlの `blog-grid` セクション内に記事カードを追加する。

### 記事カードテンプレート:
```html
<a href="articles/ファイル名.html" class="blog-card">
  <img src="https://images.unsplash.com/photo-XXXXX?w=600&h=300&fit=crop" alt="記事タイトル" loading="lazy">
  <div class="blog-body">
    <div class="blog-date">YYYY-MM-DD</div>
    <h3>記事タイトル</h3>
    <p>記事の冒頭要約（80文字程度）...</p>
    <span class="read-more">続きを読む &rarr;</span>
  </div>
</a>
```

### ルール:
- blog-grid内の記事は**最大6件**まで（古いものから削除）
- 新しい記事は**先頭**に追加
- サムネイル画像は必ずUnsplashから取得

## sitemap.xml更新方法

新しい記事を追加するたびに、sitemap.xmlに以下のエントリを追加:
```xml
<url>
  <loc>https://musclelove-777.github.io/physique-girls-navi/articles/ファイル名.html</loc>
  <lastmod>YYYY-MM-DD</lastmod>
  <priority>0.7</priority>
</url>
```

## コミットメッセージ形式

```
[auto] Add daily articles YYYY-MM-DD
```

## 毎日の更新フロー

1. CLAUDE.mdを読んで方針を確認
2. WebSearchで最新ニュースを検索
3. 記事3本を生成してarticles/に保存
4. index.htmlのblog-gridを更新（最新6件を維持）
5. sitemap.xmlを更新
6. git add, commit, push

## 広告カード必須ルール
- 全記事とindex.htmlのフッター直前に MuscleLove広告カード（ML_PROMO_CARDマーカー）を必ず含める（テンプレのカードHTML参照）。広告カードにはX / Patreon / ゲームポータルの3導線を必ず入れる。
