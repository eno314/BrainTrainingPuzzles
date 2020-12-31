# ボウリングのスコアを計算する

## TODO

- [x] 1フレーム2回投球ができ、10フレーム分の合計のスコアを算出する
- [x] ストライクでもスペアでもない場合、1投目と2投目の合計の値が、合計のスコアに加算される
- [x] ストライクの場合、1投目と2投目の合計の値に次の2投分の点数を加算した値が、合計のスコアに加算される
- [x] スペアの場合、1投目と2投目の合計の値に次の1投分の点数を加算した値が、合計のスコアに加算される
- [x] 最後のフレーム(10フレーム目)だけは、ストライクかスペアがあった場合は3回投げられる

## ユースケース

### 正常系

1. システムは、ボーリングの全フレームの点数一覧を、2次元のリスト(List[List[int]])で受け取る
1. システムは、受け取ったリストを使って、ボーリングのスコアを計算する
1. システムは、計算したボーリングのスコアを返却する

### 異常系

- [x] 受け取った点数一覧が10件じゃない場合_エラーを発生させる
- [x] 受け取った点数一覧の、1~9件目の点数が不正の場合_エラーを発生させる
  - [x] 点数がない
  - [x] 点数が3つ以上ある
  - [x] 1投目が10じゃないのに、点数が1つしかない
  - [x] 1投目が10なのに、点数が2つ以上ある
- [x] 受け取った点数一覧の、10件目の点数が不正の場合_エラーを発生させる
  - [x] 点数がない
  - [x] 点数が1つしかない
  - [x] 点数が4つ以上ある
  - [x] 1投目が10なのに、点数が2つしかない
  - [x] 1投目と2投目の合計が10なのに、点数が2つしかない
  - [x] 1投目と2投目の合計が10未満なのに、点数が3ある