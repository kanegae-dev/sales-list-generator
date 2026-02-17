"""
Sales List Generator - Main Script

東京都の指定区 × 指定キーワードでGoogle Maps API検索を行い、
重複除外後にCSV形式で出力する。

- search.py  : Google Maps API検索処理
- export.py  : CSV出力処理
- config.py  : APIキー管理
"""

from search import search_places
from export import export_csv
from config import GOOGLE_MAPS_API_KEY


# ==========================
# 設定値
# ==========================

WARDS = [
    "世田谷区",
    "目黒区",
    "大田区",
    "杉並区",
    "練馬区",
    "中野区",
    "板橋区",
    "北区",
    "足立区",
    "葛飾区",
    "江戸川区",
]

KEYWORDS = [
    "再生医療 クリニック",
    "幹細胞治療 クリニック",
]

LIMIT_PER_QUERY = 25
MAX_RESULTS = 200


# ==========================
# データ収集処理
# ==========================

def collect_places():
    """
    指定区 × キーワードで検索を行い、
    重複を除外した結果を返す。
    """
    all_results = []
    seen_place_ids = set()

    for ward in WARDS:
        for keyword in KEYWORDS:
            query = f"{ward} {keyword}"
            print("検索中:", query)

            results = search_places(
                query=query,
                api_key=GOOGLE_MAPS_API_KEY,
                limit=LIMIT_PER_QUERY
            )

            for r in results:
                place_id = r.get("place_id")

                # 重複除外
                if place_id in seen_place_ids:
                    continue

                seen_place_ids.add(place_id)

                # 区情報を追加
                r["ward"] = ward
                all_results.append(r)

                # 上限制御
                if len(all_results) >= MAX_RESULTS:
                    return all_results

    return all_results


# ==========================
# メイン処理
# ==========================

def main():
    results = collect_places()

    print("最終取得件数:", len(results))

    # CSV出力前に内部用IDを削除
    for r in results:
        r.pop("place_id", None)

    export_csv(results)


if __name__ == "__main__":
    main()
