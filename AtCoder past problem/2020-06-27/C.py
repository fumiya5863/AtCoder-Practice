N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = [0]*(N+1)
b = [0]*(M+1)
for n in range(N):
    a[n+1] = a[n] + A[n]
for m in range(M):
    b[m+1] = b[m] + B[m]
ans, j = 0, M
for i in range(N + 1):
    if a[i] > K:
        break
    while b[j] > K - a[i]:
        j -= 1
    if ans < i + j:
        ans = i + j
print(ans)