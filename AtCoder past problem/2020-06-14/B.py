X, Y = map(int, input().split())
res = False
for x in range(X+1):
    D = X - x
    if Y == (x*2 + D*4):
        res = True
if res:
    print('Yes')
else:
    print('No')
