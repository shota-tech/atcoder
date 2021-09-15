X = int(input())
sum = 100
year = 0

while sum < X:
    sum *= 1.01
    sum = int(sum)
    year += 1

print(year)