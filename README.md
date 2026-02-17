# Sales List Generator

Pythonを用いた営業リスト自動生成ツールです。

Google Places APIおよびWebスクレイピングを活用し、
指定条件に合う企業情報を自動取得・整形し、CSV形式で出力します。

---

## 🚀 開発背景

営業リスト作成の手作業負担を削減するために開発。

従来の
「Google検索 → 情報コピー → Excel貼り付け」
という作業を自動化し、

検索 → 情報取得 → 重複除外 → 整形 → CSV出力

までを一気通貫で処理します。

---

## 🛠 使用技術

- Python 3.x
- Google Places API
- requests
- CSV出力処理
- 環境変数による安全なAPIキー管理

---

## 📊 処理フロー

1. 検索条件生成（区 × キーワード）
2. Google Places API検索
3. place_idによる重複除外
4. データ整形
5. CSVファイル出力

---

## 📂 ディレクトリ構成

sales-list-generator/
│
├── main.py # 実行エントリーポイント
├── search.py # Google Places API検索処理
├── export.py # CSV出力処理
├── config.py # 環境変数管理
├── requirements.txt
└── README.md


---

## 🔐 APIキー管理

APIキーは環境変数で管理しています。

### macOS / Linux

export GOOGLE_MAPS_API_KEY="your_api_key"


### Windows

set GOOGLE_MAPS_API_KEY=your_api_key


---

## ▶ 実行方法

1. 依存パッケージをインストール

pip install -r requirements.txt


2. APIキーを設定

3. 実行

python main.py


---

## 📌 今後の拡張予定

- Webスクレイピングによる追加情報取得
- GUI化
- 条件フィルタリングの高度化
- DB保存機能追加
- SaaS化検討

---

## 👤 Author

kanegae-dev  
Pythonを用いた業務効率化・データ抽出ツール開発を行っています。
Google Maps API / Webスクレイピング / データ自動化が得意分野です。
