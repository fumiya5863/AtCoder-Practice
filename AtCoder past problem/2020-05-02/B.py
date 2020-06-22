X = int(input())
num = 100
i = 0
while True:
    if num >= X:
        break
    sun = num  // 100
    num += sun
    i += 1
print(i)

X = int(input())
num = 100
i = 0
while num < X:
    num += num // 100
    i += 1
print(i)
