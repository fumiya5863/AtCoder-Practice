A = list(map(int, input().split()))
if A[0] == 0:
    print(1)
elif A[1] == 0:
    print(2)
elif A[2] == 0:
    print(3)
elif A[3] == 0:
    print(4)
elif A[4] == 0:
    print(5)
print(15 - sum(list(map(int, input().split()))))
