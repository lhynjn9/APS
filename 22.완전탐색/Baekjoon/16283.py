import sys
sys.stdin = open('input.txt')

a, b, n, w = map(int, input().split())
res = []

for i in range(1, n):
    if (i*a) + ((n-i) * b) == w:
        res.append([i, n-i])

if len(res) != 1:
    print(-1)
else:
    print(*res[0])