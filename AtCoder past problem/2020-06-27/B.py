S = input()
T = input()
N = len(S)
cnt = 0

# 文字が等しくない時に変更
for n in range(N):
    if S[n] != T[n]:
        cnt += 1
print(cnt)