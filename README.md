### robosys2025

## adfgコマンド
![test](https://github.com/naiunaiu/robosys2025/actions/workflows/test.yml/badge.svg)

入力テキストをADFGVX暗号で暗号化、復号するコマンド

## 使い方
- 暗号化
  ```
  $ echo aiueo | adfg　
  AA_DF_GF_AV_FF

  #もしくは

  $ adfg
  kakikukeko sasisuseso #ここでテキストを入力
  DV_AA_DV_DF_DV_GF_DV_AV_DV_FF_GA_AA_GA_DF_GA_GF_GA_AV_GA_FF
  ```
- 復号
  ```
  $ echo AA_DF_GF_AV_FF | adfg
  aiueo

  #もしくは

  $ adfg
  DV_AA_DV_DF_DV_GF_DV_AV_DV_FF_GA_AA_GA_DF_GA_GF_GA_AV_GA_FF
  kakikukeko sasisuseso
  ```
## 注意
- 暗号化できる文字は半角小文字アルファベットと、半角数字のみ。
- 暗号化する文字列は、半角空白のみで繋げる。
  ```
  $ echo aiueo waon | adfg #これならOK
  $ echo aiueo_waon | adfg
    Wrong Input. #半角空白以外だとエラー
  ```
- 復号する際は使い方の項目で示されている出力例と同じ書式の暗号文を入力する。

## インストール方法
```
$ git clone https://github.com/naiunaiu/ADFGVX.git
```

## 必要なソフトウェア
- Python
  - Python 3.7~3.10で検証済み

## テスト環境
  - Ubuntu 24.04 LTS

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- © 2025 Satoh Narumi
