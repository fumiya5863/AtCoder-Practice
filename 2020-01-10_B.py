N = int(input())
S = input()
cnt = 0
for n in range(N-2):
    if S[n] == 'A' and S[n+1] == 'B' and S[n+2] == 'C':
        cnt += 1
print(cnt)