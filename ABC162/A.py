x = int(input())
flg = False
while x:
    if x % 10 == 7:
        flg = True
        break
    x //= 10
if flg:
  print('Yes')
else:
  print('No')