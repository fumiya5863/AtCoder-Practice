N = int(input())
list1 = []
list2 = []
for n in range(N):
    x, c = input().split()
    if c == 'R':
        x = int(x)
        list1.append(x)
    else:
        x = int(x)
        list2.append(x)
list1.sort()
list2.sort()
mylist = list1 + list
for i in mylist:
    print(i)