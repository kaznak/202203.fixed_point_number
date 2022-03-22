
# fixed_point_number

## 仕様

- 以下の理由から有理数に寄せて実装。
  - python の integer は無限精度[^1]
  - 2 だけではなく色々なスケーリング係数が使われるケースがあるらしい[^2]

[^1]: [Integers have unlimited precision.](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
[^2]: [Fixed-point formats with scaling factors of the form 2n-1 (namely 1, 3, 7, 15, 31, etc.) have been said to be appropriate for image processing and other digital signal procssing tasks.](https://en.wikipedia.org/wiki/Fixed-point_arithmetic#Choice_of_scaling_factors)

- 除算は整除法で実装
- 乗算、除算に伴う桁溢れは、剰余を切り捨て

## 実装

スケーリング係数が同じ場合、異なる場合のそれぞれについて演算を実装。

- `fixed_point_number.py`
    - 固定小数点数クラスの実装
- `arith_fixed.py`
    - スケーリング係数が同じ場合のみ演算
    - モジュールがエクスポートするのはこちら
- `arith_autoscale.py`
    - スケーリング係数が異なる場合も演算

## テスト

[python poetry](https://python-poetry.org/) を使用。

`test/` 以下に配置。

```
poetry install
poetry run pytest
```

## reference

- [Fixed-point arithmetic](https://en.wikipedia.org/wiki/Fixed-point_arithmetic)
- [Numeric Types — int, float, complex](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
