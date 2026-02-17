"""
Export Module

検索結果をCSVファイルに出力する。
"""

import csv
from typing import List, Dict


OUTPUT_FILE = "results.csv"


def export_csv(data: List[Dict]) -> None:
    """
    データをCSV形式で保存する。

    :param data: 出力対象データ
    """

    if not data:
        print("No data to export.")
        return

    fieldnames = data[0].keys()

    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Export completed: {OUTPUT_FILE}")
