# 計算量が間に合わない
N, A, B = map(int, input().split())
a = 0
C = 0
# Nが0になるまでループ処理
while N > 0:
    C = N
    N = N - A
    if N > 0:
        a = a + A
    else:
        a = a + C
    N = N - B
print(a)

# 計算量が間に合う
N, A, B = map(int, input().split())
# N個の個数からAを何個取りだせるか
ans = N // (A + B) * A
rem = N % (A + B)
ans += min(rem, A)
print(ans)
