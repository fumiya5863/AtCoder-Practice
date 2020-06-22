N = int(input())
Q = int(input())
string = input()
S = [0]*(N+1)
for n in range(N):
    if n + 1 < N and string[n] == 'A' and string[n+1] == 'C':
        S[n+1] = S[n] + 1
    else:
        S[n+1] = S[n]
for q in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(S[r] - S[l])