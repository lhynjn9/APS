import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(a):
    Q = deque()
    Q.append(a)

    while Q:
        a = Q.popleft()
        for w in G[a]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[a] + 1

n = int(input()) # 사람 수
a, b = map(int, input().split()) # 촌수 계산해야 하는 사람 수
m = int(input()) # 부모 자식들간의 관계 수
G = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split()) # 부모 자식 번호
    G[x].append(y)
    G[y].append(x)

bfs(a)

print(visited[b] if visited[b] > 0 else -1)
