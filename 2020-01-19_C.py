# N = int(input())
# P = list(map(int, input().split()))
# cnt = 0
# for n in range(N):
#     res = True
#     for i in range(n):
#         if P[n] > P[i]:
#             res = False
#             break
#     if res:
#         cnt += 1
# print(cnt)

N = int(input())
P = list(map(int, input().split()))
cnt = 0
res = float('Inf')
for n in range(N):
    if P[n] <= res:
        res = P[n]
        cnt += 1
print(cnt)