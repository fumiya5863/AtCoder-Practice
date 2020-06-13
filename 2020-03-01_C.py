N, M = map(int, input().split())
A = []
cnt = -1
man = False
for m in range(M):
    s, c = map(int, input().split())
    A.append([s, c])
for n in range(1000):
    num = str(n)
    res = True
    if len(num) != N:
        continue
    for m in range(M):
        if num[A[m][0]-1] != str(A[m][1]):
            res = False
    if res:
        cnt = int(num)
        man = True
        break
if man:
    print(cnt)
else:
    print(cnt)