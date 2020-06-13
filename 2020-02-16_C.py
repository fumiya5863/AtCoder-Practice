# N = int(input())
# A = []
# for n in range(N):
#     A.append(input())
# B = []
# A.sort()
# p = 1
# for n in range(N):
#     C = 0
#     for i in range(p, N):
#         if A[n] == A[i]:
#             C += 1
#     B.append(C)
#     p += 1
# maxv = max(B)
# D = []
# for n in range(N):
#     if maxv == B[n]:
#         D.append(A[n])
# for d in D:
#     print(d)

# N = int(input())
# A = {}
# B = []
# for n in range(N):
#     a = input()
#     B.append(a)
#     A[a] = 0
# for n in range(N):
#     A[B[n]] += 1
# res = 0
# C = []
# for key, value in A.items():
#     if res < value:
#         res = value
# for key, value, in A.items():
#     if res == value:
#         C.append(key)
# C.sort()
# for c in C:
#     print(c)
