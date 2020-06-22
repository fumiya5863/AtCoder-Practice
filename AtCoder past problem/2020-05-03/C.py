N, M = map(int, input().split())
H = list(map(int, input().split()))
cnt = 0
l = [0]*N
AB = list()
for m in range(M):
    P = list(map(int, input().split()))
    AB.append(P)
for m in range(M):
    if H[AB[m][0]-1] < H[AB[m][1]-1]:
        l[AB[m][0]-1] += 1
    elif H[AB[m][0]-1] > H[AB[m][1]-1]:
        l[AB[m][1]-1] += 1
    elif H[AB[m][0]-1] == H[AB[m][1]-1]:
        l[AB[m][0]-1] += 1
        l[AB[m][1]-1] += 1
for i in l:
    if i == 0:
        cnt += 1
print(cnt)

n, m = map(int, input().split())
H = [int(i) for i in input().split()]
ans = [True]*n
for  i in range(m):
    a, b = map(int, input().split())
    if H[a-1] < H[b-1]:
        ans[a-1] = False
    elif H[a-1] > H[b-1]:
        ans[b-1] = False
    elif H[a-1] == H[b-1]:
        ans[a-1] = False
        ans[b-1] = False
print(ans.count(True))