import sys
sys.stdin = open('input.txt')

M = int(input())
S = set()

for i in range(M):
    lst = sys.stdin.readline().strip().split()

    if len(lst) == 1:
        if lst[0] == 'all':
            S = set([i for i in range(1, 21)])
        else:
            S = set()
        continue

    a, x = lst[0], int(lst[1])

    if a == 'add':
        S.add(x)
    elif a == 'remove':
        S.discard(x)
    elif a == 'check':
        print(1 if x in S else 0)
    elif a == 'toggle':
        if x in S:
            S.discard(x)
        else:
            S.add(x)



