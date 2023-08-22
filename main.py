import csv
import sys
import os
import re
from ibm_watson import DiscoveryV2

if __name__ == "__main__":

    # ファイル作成前に古いファイルをoldに移動する。
    os.system("./clean-output.sh")

    # 第一引数として検索文字列受け取る
    query = sys.argv[1]

    discovery = DiscoveryV2(
        version='2020-08-30')

    response = discovery.query(
        project_id="<REPLACE_PROJECT_ID>",
        natural_language_query=query,
        # highlight=True,
        # count=5
    ).get_result()

    csv_data = []
    for result in response["results"]:
        passage = result["document_passages"][0]["passage_text"].replace(
            "<em>", "").replace("</em>", "").replace("\n", "").replace("　", " ")
        passage = re.sub("\s+", ' ', passage)
        file_name = result["extracted_metadata"]["filename"]
        csv_data.append([passage, file_name])

        # 上記の結果5件を取得したら処理終了
        if len(csv_data) > 4:
            break

    with open(f'./output/{query}.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',',  # 区切り文字はカンマ
                            quotechar='"',  # 囲い文字はダブルクォーテーション
                            quoting=csv.QUOTE_NONNUMERIC)  # 全ての非数値フィールドをクオート
        for row in csv_data:
            writer.writerow(row)

    print("Request completed successfully.")
    print(f"Open created file: ./output/{query}.csv")
