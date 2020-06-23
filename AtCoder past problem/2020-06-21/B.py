N, K = map(int, input().split())
P = list(map(int, input().split()))
P.sort()
res = 0
for k in range(K):
    res += P[k]
print(res)
    