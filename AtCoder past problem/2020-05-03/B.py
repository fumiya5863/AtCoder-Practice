N, K = map(int, input().split())
l = [0]*N
cnt = 0
for i in range(K):
    D = int(input())
    a = list(map(int, input().split()))
    for d in range(D):
        l[a[d]-1] += 1
for i in l:
    if i == 0:
        cnt += 1
print(cnt)
