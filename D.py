from collections import deque

S = input()
B = deque()
res = 0
for s in range(len(S)):
    B.append(S[s])
Q = int(input())
for q in range(Q):
    A = list(map(str, input().split()))
    if int(A[0]) == 1:
        if res == 0:
            res = 1
        else:
            res = 0
    else:
        if int(A[1]) == 1:
            if res == 0:
                B.appendleft(A[2])
            else:
                B.append(A[2])
        else:
            if res == 0:
                B.append(A[2])
            else:
                B.appendleft(A[2])
if res == 0:
    print(''.join(B))
else:
    B.reverse()
    print(''.join(B))


    
                