N, K, M = map(int, input().split())
A = list(map(int, input().split()))
l = 0
for a in A:
    l += a
res = False
for k in range(K+1):
    l += k
    if l // N >= M:
        print(k)
        res = True
        break
    l -= k
if res == False:
    print(-1)