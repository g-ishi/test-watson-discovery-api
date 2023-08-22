# call-watson-discovery

Watson Discovery の API をコールして、結果を CSV ファイルに出力するサンプルプログラムです。

Watson Discovery を試してみるためのリポジトリです。

## How to use

0. prerequisites

   python3 が必要です。(python3.9 で動作確認をしています。)

1. 必要なパッケージのインストール

   ```sh
   $ pip3 install --upgrade "ibm-watson>=6.1.0"
   ```

2. 資格情報の配置

   [こちら](https://github.com/watson-developer-cloud/python-sdk#credential-file)を参考に、リポジトリ直下に`ibm-credentials.env`を配置します。

3. プログラムの実行

   ```sh
   $ python3 main.py "{検索文字列}"
   ```

実行結果は`./output/{検索文字列}.csv`ファイルに出力されます。

5. 補足

- ファイル出力する結果は、プログラム側で 5 件に制限しています。
# test-watson-discovery-api
