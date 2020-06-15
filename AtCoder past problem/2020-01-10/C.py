import itertools
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
a = 0
b = 0
cnt = 0
for n in itertools.permutations(range(1, N+1)):
    if P == list(n):
        a = cnt
    if Q == list(n):
        b = cnt
    cnt += 1
total = abs(a-b)
print(total)
