import math

A, B, H, M = map(int, input().split())

diff = abs(30 * H + 0.5 * M - 6 * M)
rad = math.radians(diff)
ans = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(rad))

print(ans)