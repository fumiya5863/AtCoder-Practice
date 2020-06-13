N, M = map(int, input().split())
AC = [0]*N
WA = [0]*N
L = []
for m in range(M):
    p, S = map(str, input().split())
    p = int(p)
    L.append([p, S])
for m in range(M):
    if not AC[L[m][0]-1] == 0:
        continue    
    if L[m][1] == 'AC':
        AC[L[m][0]-1] = 1
    elif L[m][1] == 'WA':
        WA[L[m][0]-1] += 1
A = sum(AC)
W = sum(WA)
for n in range(N):
    if AC[n] == 1:
        W += WA[n]
print(A, W)

n, m = map(int, input().split())
tmp  = [0]*n
wtmp = [0]*n
for _ in range(m):
    P, s = map(str, input().split())
    p = int(P)
    p -= 1
    if not tmp[p] == 0:
        continue
    if s == 'AC':
        tmp[p] = 1
    else:
        wtmp[p] += 1
ans1 = sum(tmp)
ans2 = 0
for i in range(n):
    if tmp[i] == 1:
        ans2 += wtmp[i]
print(ans1, ans2)
