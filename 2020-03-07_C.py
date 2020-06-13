import math
A, B = map(int, input().split())
res = -1
for n in range(100**2):
    if math.floor(n * 0.08) == A:
        if math.floor(n * 0.1) == B:
            res = n
            break
print(res)