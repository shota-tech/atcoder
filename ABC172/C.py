n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
time = 0
cnt = 0
while True:
    if a and b:
        if a[0] < b[0]:
            time += a.pop(0)
            if time > k:
                break
            cnt += 1
        else:
            time += b.pop(0)
            if time > k:
                break
            cnt += 1
    elif a:
        time += a.pop(0)
        if time > k:
            break
        cnt += 1
    elif b:
        time += b.pop(0)
        if time > k:
            break
        cnt += 1
    else:
        break

print(cnt)