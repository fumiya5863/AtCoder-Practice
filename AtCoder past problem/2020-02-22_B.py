N, K = map(int, input().split())
A = ''
while N > 0:
    N = N // K
    B = N % K
    A = A + str(B)
print(len(A))
