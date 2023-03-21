import sys
sys.stdin = open('input.txt')

N = int(input())

lst = [[0] * 101 for _ in range(101)]
res = 0

for i in range(N):
    x, y = map(int, input().split())

    for a in range(x, x+10):
        for b in range(y, y+10):
            lst[a][b] = 1

for a in lst:
    res += a.count(1)

print(res)