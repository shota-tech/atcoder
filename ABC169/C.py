import math
from decimal import Decimal
A, B = input().split()
A = int(A)
B = Decimal(B)
ans = math.floor(A * B)
print(ans)