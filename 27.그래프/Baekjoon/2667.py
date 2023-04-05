import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(input())
lst = [list(map(int, input())) for _ in range(N)]
# 방문 체크
visited = [[0] * N for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
check = 0
Q = deque()
res = []

for i in range(N):
    for j in range(N):
        # 체크 되어 있는 곳 중에서 아직 방문 안한 경우에는 Q에 삽입
        if lst[i][j] == 1 and visited[i][j] == 0:
            check += 1
            visited[i][j] = check # 방문 체크
            lst[i][j] = 0
            Q.append((i, j))
            x = 1
            while Q:
                a, b = Q.popleft()
                for k in d:
                    ar, br = a + k[0], b + k[1]
                    if 0 <= ar < N and 0 <= br < N and visited[ar][br] == 0 and lst[ar][br] == 1:
                        visited[ar][br] = check
                        lst[i][j] = 0
                        Q.append((ar, br))
                        x += 1
            res.append(x)

print(check)
res.sort()
for p in res:
    print(p)

