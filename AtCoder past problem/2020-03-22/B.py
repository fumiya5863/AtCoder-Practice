S = input()
N = len(S)
P = []
L = []
K = []
for s in range(N):
    P.append(S[s])
L = P[:(N-1)//2]
K = P[(N+3)//2-1:N]
if L == K:
    print('Yes')
else:
    print('No')
