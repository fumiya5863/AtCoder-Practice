A, B, C, K = map(int, input().split())
xa = min(A, K)
K = K - xa
xb = min(B, K)
K = K - xb
xc = min(C, K)
total = xa*1 + xb*0 + xc*-1
print(total)
