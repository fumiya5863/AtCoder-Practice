A = []
cnt = False
for n in range(3):
    a = list(map(int, input().split()))
    A.append(a)
N = int(input())
B = []
for n in range(N):
    b = int(input())
    B.append(b)
for i in range(3):
    for j in range(3):
        for n in range(N):
            if A[i][j] == B[n]:
                A[i][j] = 0
for i in range(3):
    if A[i][0] == 0 and A[i][1] == 0 and A[i][2] == 0:
        cnt = True
for i in range(3):
    if A[0][i] == 0 and A[1][i] == 0 and A[2][i] == 0:
        cnt = True
if A[0][0] == 0 and A[1][1] == 0 and A[2][2] == 0:
    cnt = True
if A[0][2] == 0 and A[1][1] == 0 and A[2][0] == 0:
    cnt = True
if cnt:
    print('Yes')
else:
    print('No')
