N, M = map(int, input().split())
cnt = 0
cnt += N * (N - 1) // 2
cnt += M * (M - 1) // 2
print(cnt)