### robosys2025

## gazoコマンド
![test](https://github.com/naiunaiu/robosys2025/actions/workflows/test.yml/badge.svg)

入力テキストをADFGVX暗号で暗号化、復号するコマンド

## 使い方
- 暗号化
  ```
  $ echo aiueo | adfg　
  AA_DF_GF_AV_FF
  #もしくは
  $ adfg
  aiueo #ここでテキストを入力
  AA_DF_GF_AV_FF
  ```
- 復号
  ```
  $ echo AA_DF_GF_AV_FF | adfg
  aiueo
  #もしくは
  $ adfg
  AA_DF_GF_AV_FF
  aiueo
  ```

## インストール方法
```git clone https://github.com/naiunaiu/gazo.git```

## 必要なソフトウェア
- Python
  - Python 3.7~3.10で検証済み

## テスト環境
  - Ubuntu 24.04 LTS

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- © 2025 Satoh Narumi
