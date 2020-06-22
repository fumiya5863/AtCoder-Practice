A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
if B > A:
    A = A + V*T
    B = B + W*T
    if A >= B:
        print('YES')
    else:
        print('NO')
else:
    A = A - V*T
    B = B - W*T
    if A <= B:
        print('YES')
    else:
        print('NO')