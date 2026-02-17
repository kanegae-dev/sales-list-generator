# Sales List Generator

Pythonを用いた営業リスト自動生成ツールです。  
Google Maps APIおよびWebスクレイピングを活用し、指定条件に合う企業情報を自動取得・整形し、CSV形式で出力します。

---

## 🚀 開発背景

営業リスト作成の手作業負担を削減するために開発。
検索 → 情報取得 → 条件フィルタ → CSV出力 までを自動化します。

---

## 🔧 主な機能

- キーワード検索による企業抽出
- Google Maps API連携
- Webスクレイピングによる追加情報取得
- 条件フィルタリング（業種・価格帯・除外条件など）
- CSV出力

---

## 🛠 使用技術

- Python
- Google Maps API
- requests / BeautifulSoup
- CSV処理

---

## 📂 今後の改善予定

- GUI化
- データベース連携
- 処理速度の最適化
