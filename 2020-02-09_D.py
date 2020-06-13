# N, K = map(int, input().split())
# P    = list(map(int, input().split()))
# res  = 0
# p    = 0
# for n in range(N - K + 1):
#     D = 0
#     for k in range(p, K + p):
#         D += (P[k] + 1) / 2
#     if res < D:
#         res = D
#     p += 1
# print(res)

# N, K = map(int, input().split())
# P    = list(map(int, input().split()))
# p    = [(P[i]+1) / 2 for i in range(N)]
# a    = 0
# for i in range(K):
#     a += p[i]
# b = a
# for i in range(N - K):
#     c = a + p[i+K] - p[i]
#     if b < c:
#         b = c
#     a = c
# print(b)