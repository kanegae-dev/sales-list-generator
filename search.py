"""
Search Module

Google Maps Places API を使用して
指定クエリに基づく施設情報を取得する。
"""

import requests
from typing import List, Dict


BASE_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"


def search_places(
    query: str,
    api_key: str,
    limit: int = 20
) -> List[Dict]:
    """
    指定クエリでGoogle Places API検索を行う。

    :param query: 検索キーワード
    :param api_key: Google Maps APIキー
    :param limit: 最大取得件数
    :return: 施設情報のリスト
    """

    results = []
    next_page_token = None

    while len(results) < limit:
        params = {
            "query": query,
            "key": api_key
        }

        if next_page_token:
            params["pagetoken"] = next_page_token

        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if "results" not in data:
            break

        for place in data["results"]:
            results.append({
                "name": place.get("name"),
                "address": place.get("formatted_address"),
                "rating": place.get("rating"),
                "place_id": place.get("place_id")
            })

            if len(results) >= limit:
                break

        next_page_token = data.get("next_page_token")

        # ページネーションがない場合終了
        if not next_page_token:
            break

    return results[:limit]
