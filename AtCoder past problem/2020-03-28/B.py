X = int(input())
C = 0
D = 0
if X >= 0 and X <= 10 ** 9:
    while True:
        if X >= 500:
            C = X // 500
            X = X - (500 * C)
        elif X >= 5:
            D = X // 5
            X = X - (5 * D)
        else:
            break
total = (1000 * C) + (5 * D)
print(total)

X = int(input())
C = 0
D = 0
if X >= 500:
    C = X // 500
    X = X - (500 * C)
if X >= 5:
    D = X // 5
total = (1000 * C) + (5 * D)
print(total)

