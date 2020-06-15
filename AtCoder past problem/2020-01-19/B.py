a, b = map(str, input().split())
A = ''
B = ''
for i in range(int(b)):
    A += a
for i in range(int(a)):
    B += b
if A < B:
    print(A)
else:
    print(B)
