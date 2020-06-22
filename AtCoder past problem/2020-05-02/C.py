import itertools
N, M, Q = map(int, input().split())
m = list()
res = -100
for i in range(Q):
    n = list(map(int, input().split()))
    m.append(n)
l = [x for x in range(1, M + 1)]
p = itertools.combinations_with_replacement(l, N)
for p in p:
    total = 0
    for i in range(Q):
        a = m[i][0]
        b = m[i][1]
        A = p[a - 1]
        B = p[b - 1]
        C = B - A
        if m[i][2] == C:
            total = total + m[i][3]
    if res < total:
        res = total
print(res)

import math
import itertools
N, M, Q = map(int, input().split())
a = [0]*Q
b = [0]*Q
c = [0]*Q
d = [0]*Q
for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())
Al = [0]*M
for i in range(M):
    Al[i] = i + 1
All = list(itertools.combinations_with_replacement(Al, N))
ans = 0
for A in All:
    wa = 0
    for i in range(Q):
        kari = A[b[i]-1] - A[a[i] - 1]
        if kari == c[i]:
            wa = wa + d[i]
    if ans < wa:
        ans = wa
print(ans)

