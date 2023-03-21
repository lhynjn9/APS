import sys
sys.stdin = open('input.txt')

N = int(input())
D = int(input())
lst = []
res = 0

for i in range(N-1):
    lst.append(int(input()))

if N == 1:
    print(res)
else:
    lst.sort(reverse=True)

    while lst[0] >= D:
        D += 1
        lst[0] -= 1
        res += 1
        lst.sort(reverse=True)

    print(res)