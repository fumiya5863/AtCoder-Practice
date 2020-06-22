X, N = map(int, input().split())
if N > 0:
    P = list(map(int, input().split()))
    A = [0]*102
    cnt = 0
    res = float('Inf')
    for n in range(N):
        A[P[n]] += 1
    for a in A:
        if a == 0:
            total = abs(X - cnt)
            if res > total:
                res = total
                man = cnt
        cnt += 1
    print(man)
else:
    print(X)