N = int(input())
A = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
]
res = []
while N > 0:
    a = (N - 1) % 26
    N = (N - 1) // 26
    res.append(A[a])
res.reverse()
print(''.join(res))

