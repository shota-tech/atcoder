import bisect
import copy
import math
import string
from decimal import Decimal, ROUND_HALF_UP
from itertools import permutations, combinations


"""
入力
"""
# 文字列 → リスト
l = list(input())
# 文字列リスト
l = input().split()
# 数値リスト → 数値
a, b = map(int, input().split())
# 数値リスト
l = list(map(int, input().split()))
# 複数行(行数指定あり)
n = input()
l = [input() for _ in range(n)]
# 複数行(行数指定なし)
l = []
while True:
    try:
        l.append(input())
    except EOFError:
        break


"""
計算
"""
# 商と余り
q, mod = divmod(10, 3)
# 四捨五入
f = 123.45
f2 = (Decimal(str(f))).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)  # 123.5

a, b = 4, 6
# 最大公約数
c = math.gcd(a, b)
# 最小公倍数
c = (a * b) // math.gcd(a, b)


"""
文字列
"""
s = "abcde"
# 終端
s[-1:]
# 終端以外
s[:-1]
# 反転
s[::-1]
# アッパーケース
s.upper()
# ローワーケース
s.lower()
# スワップケース
s.swapcase()
# カウント
s.count("a")
# 置換
s.replace("a", "b")
# アルファベット(小文字)
s = string.ascii_lowercase
# アルファベット(大文字)
s = string.ascii_uppercase
# アルファベット(小文字・大文字)
s = string.ascii_letters
# 数字
s = string.digits
# 数字(16進数)
s = string.hexdigits


"""
リスト
"""
l = ["a", "b", "c"]
# カウント
l.count("a")
# インデックス
l.index("a")
# リスト → 文字列
"".join(l)
# ソート(昇順)
l2 = sorted(l)
# ソート(降順)
l2 = sorted(l, reverse=True)
# ソート(2番目の要素)
tl = [("a", 1), ("b", 2), ("c", 3)]
tl2 = sorted(tl, key=lambda x: x[1])
# 反転
l2 = list(reversed(l))
# 一次元配列コピー
l2 = l[:]
# 二次元配列コピー
l2 = copy.deepcopy(l)

a = [2, 4, 6, 8]
b = [3, 6, 9]
# 和集合
c = list(set(a) | set(b))
# 積集合
c = list(set(a) & set(b))


"""
アルゴリズム
"""
l = ["a", "b", "c"]
# 順列
l2 = list(permutations(l, 2))
# 組み合わせ
l2 = list(combinations(l, 2))

# bit全探索(部分集合全パターン列挙)
items = ["apple", "orange", "banana"]
n = len(items)
for bit in range(1 << n):
    shopping_list = []
    for i in range(n):
        if bit & (1 << i):
            shopping_list.append(items[i])
    print(shopping_list)

# 二分探索
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = bisect.bisect_left(l, 8)
