# fetch

# fetchコマンド
![test](https://github.com/naiunaiu/fetch/actions/workflows/test.yml/badge.svg)

カレントディレクトリに指定したファイルをコピー/移動させるコマンド。

# 使い方
- コマンド
  - [fetch <オプション> <コピー/移動したいファイルの場所> <ファイルの名前>]
-　オプション
  - -m … ファイルを移動させる。移動前の場所にファイルは残らない。
  - -c … ファイルをコピーする。移動前の場所にもファイルが残る。
  - 実行後、とってきたファイルのディレクトリが表示されますが仕様です。

# インストール方法
  - githubが手元にある…git clone https://github.com/naiunaiu/fetch.git　これをlinuxで実行することで使用可能。

  - github持ってない…このリポジトリからzipファイルをダウンロードし、中身のfetchをusr/binに配置する。

# 必要なソフトウェア
- Python
  - Python 3.7~3.10で検証済み

# テスト環境
  - Ubuntu 24.04 LTS


# 著作権
  - このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。

  - © 2025 Satoh Narumi
