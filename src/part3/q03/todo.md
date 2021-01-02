# 同じ数を表示し続ける7セグメントディスプレイ

## TODO

- [x] 数字を7セグメントディスプレイで表示した際に、点灯している場所の数を取得する
  - [x] 0の場合は6
  - [x] 1の場合は2
  - [x] 2の場合は5
  - [x] 3の場合は5
  - [x] 4の場合は4
  - [x] 5の場合は5
  - [x] 6の場合は6
  - [x] 7の場合は3
  - [x] 8の場合は7
  - [x] 9の場合は6
  - [x] 0より小さい数の場合はエラー
  - [x] 9より大きい数の場合はエラー
- [x] ある数字の各桁での点灯数の積を算出する ... a
  - [x] 718の場合は42(3 * 2 * 7)
  - [x] 1桁の場合は点灯数を返す
  - [x] 0より小さい場合はエラー
- [x] aを、繰り返し、登場する数がいくつかるか数える
  - [x] 718の場合は、718, 42, 20, 30, 30, 30, ... となるので、の4つ
  - [x] 100の場合は、100, 72, 15, 10, 12, 10, 12, 10, 12... となるので、5つ