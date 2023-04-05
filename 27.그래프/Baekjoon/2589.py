import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(x, y):
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    cnt = 0
    Q = deque()
    Q.append((x, y))

    while Q:
        a, b = Q.popleft()
        for k in d:
            ar, br = a + k[0], b + k[1]
            if 0 <= ar < N and 0 <= br < M and visited[ar][br] == 0 and lst[ar][br] == 'L':
                visited[ar][br] = visited[a][b] + 1
                cnt = max(cnt, visited[ar][br])
                Q.append((ar, br))

    return cnt - 1

N, M = map(int, sys.stdin.readline().split())
lst = [list(sys.stdin.readline()) for _ in range(N)]
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
res = 0

for i in range(N):
    for j in range(M):
        if lst[i][j] == 'L':
            res = max(res, bfs(i, j))

print(res)