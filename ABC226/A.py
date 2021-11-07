from decimal import Decimal, ROUND_HALF_UP
x = Decimal(input())
ans = x.quantize(Decimal('0'), rounding=ROUND_HALF_UP)
print(ans)