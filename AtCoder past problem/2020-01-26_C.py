N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort()
for k in range(K):
    if H:
        H.pop(len(H)-1)
H = sum(H)
print(H)
