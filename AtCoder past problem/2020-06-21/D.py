#  辞書で解いた
N = int(input())
A = list(map(int, input().split()))
C = sum(A)
Z = {}
for n in range(N):
    Z[A[n]] = 0
for n in range(N):
    Z[A[n]] += 1
D = []
Q = int(input())
for q in range(Q):
    x, y = map(int, input().split())
    if x in Z:
        C = C - x*Z[x]
        C = C + y*Z[x]
        D.append(C)
        if y in Z:
            Z[y] += 1*Z[x]
        else:
            Z[y] = Z[x]
        Z.pop(x)
    else:
        D.append(C)
for d in D:
    print(d)