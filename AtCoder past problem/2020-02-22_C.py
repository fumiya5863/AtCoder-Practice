N = int(input())
X = list(map(int, input().split()))
M = max(X)
res = float('Inf')
for m in range(1, M+1):
    total = 0
    for x in X:
        total += (x - m)**2
    if res > total:
        res = total
print(res)