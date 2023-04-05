from collections import deque
import sys
sys.stdin = open('input.txt')

N = int(input())
lst = []
maxH = 0

for _ in range(N):
    low = list(map(int, input().split()))
    lst.append(low)

    for c in low:
        if c > maxH:
            maxH = c


def rain(x):
    for i in range(N):
        for j in range(N):
            if lst[i][j] <= x:
                visited[i][j] = 0

    return


def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    visited[x][y] = 0

    while Q:
        a, b = Q.popleft()
        for k in d:
            ar, br = a + k[0], b + k[1]
            if 0 <= ar < N and 0 <= br < N and visited[ar][br] == 1:
                visited[ar][br] = 0
                Q.append((ar, br))

    return


res = 0
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(maxH):
    visited = [[1] * N for _ in range(N)]
    rain(i)  # 잠긴 곳을 0으로 표시

    # 안전한 영역을 셈
    x = 0
    for p in range(N):
        for q in range(N):
            if visited[p][q] == 1:
                bfs(p, q)
                x += 1

    res = max(res, x)

print(res)