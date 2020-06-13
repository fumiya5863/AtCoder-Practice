H = int(input())
res = 0
cnt = 1
while H > 0:
    H = H // 2
    if res == 0:
        res = 1
    else:
        cnt *= 2
        res += cnt
print(res)