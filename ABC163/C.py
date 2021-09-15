N = int(input())
l = list(map(int, input().split()))

nums = [0 for i in range(N)]

for e in l:
    nums[e-1] += 1

for num in nums:
    print(num)