K = int(input())
A, B = map(int, input().split())
res = False
for i in range(1000):
    k = i * K
    if k >= A and k <= B:
        res = True
if res:
    print('OK')
else:
    print('NG')

K = int(input())
A, B = map(int, input().split())
largest = (B // K) * K
if largest >= A:
    print('OK')
else:
    print('NG')