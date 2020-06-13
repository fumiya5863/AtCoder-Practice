# N = int(input())
# A = list(map(int, input().split()))
# res = True
# p = 1
# for n in range(N):
#     for i in range(p, N):
#         if A[n] == A[i]:
#             res = False
#     p += 1
# if res:
#     print('YES')
# else:
#     print('NO')

N = int(input())
A = list(map(int, input().split()))
A.sort()
res = A[0]
cnt = True
for n in range(1, N):
    if A[n] == res:
        cnt= False
    res = A[n]
if cnt:
    print('YES')
else:
    print('NO')