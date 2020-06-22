K = int(input())
S = input()
T = ''
if len(S) <= K:
    print(S)
else:
    for i in range(K):
        T += S[i]
    print('{}{}'.format(T, '...'))

k = int(input())
s = input()
if len(s) > k:
    s = s[:k] + "..."
    print(s)
else:
    print(s)

