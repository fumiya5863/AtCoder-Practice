S, L, R = map(int, input().split())

while True:
    if L <= S <= R:
        print(S)
        break

    if S < L:
        S += 1
    elif S > R:
        S -= 1 