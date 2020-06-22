import math
A, B, H, M = map(int, input().split())
p = 0
o = 0
for i in range(1, H+1):
    p += 30
for q in range(1, M+1):
    o += 6
y = M * 0.5
p = p + y
H = abs(o - p)
total = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(math.radians(H)))
print(total)
