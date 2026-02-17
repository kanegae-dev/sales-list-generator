# 🚀 Sales List Generator

Pythonを用いた営業リスト自動生成ツールです。  
Google Maps APIおよびWebスクレイピングを活用し、指定条件に合う企業情報を自動取得・整形し、CSV形式で出力します。

---

## 🎯 開発背景

営業リスト作成の手作業負担を削減するために開発。  

従来：
検索 → 情報収集 → 重複除外 → 整形 → CSV出力  
をすべて手動で実施。

本ツールではこれらを自動化し、  
**作業時間の大幅削減と精度向上を実現**します。

---

## 🛠 使用技術

- Python 3.x
- Google Places API
- requests
- CSV出力処理
- 環境変数による安全なAPIキー管理

---

## 📂 ディレクトリ構成

```
sales-list-generator/
├── main.py          # 実行エントリーポイント
├── search.py        # Google Places API検索処理
├── export.py        # CSV出力処理
├── config.py        # 環境変数管理
├── requirements.txt
└── README.md
```

---

## 🔐 APIキー管理

APIキーは環境変数で管理しています。

### macOS / Linux

```
export GOOGLE_MAPS_API_KEY="your_api_key"
```

### Windows (PowerShell)

```
setx GOOGLE_MAPS_API_KEY "your_api_key"
```

---

## ▶ 実行方法

### 1. パッケージインストール

```
pip install -r requirements.txt
```

### 2. 実行

```
python main.py
```

---

## ⚙ 処理フロー

1. 検索条件生成（区 × キーワード）
2. Google Places API検索
3. 重複除外（place_id）
4. データ整形
5. CSV出力

---

## ✨ 特徴

- 重複排除ロジック搭載
- 最大取得件数制御
- APIキーの安全管理
- モジュール分離による拡張性設計
- 再生医療・幹細胞クリニックに特化した抽出ロジック

---

## 📌 今後の拡張予定

- Webスクレイピング強化
- フィルタリング機能追加
- GUI対応
- ログ管理機能

---

## 👤 Author

kanegae-dev  
Pythonによる業務自動化・データ抽出ツール開発

