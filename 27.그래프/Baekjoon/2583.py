import sys
sys.stdin = open('input.txt')

M, N, K = map(int, input().split())
lst = [[0] * N for _ in range(M)]
Q = []
res = 0 # 개수
check = [] # 몇개인지

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            if lst[i][j] == 0:
                lst[i][j] = -1

for x in range(M):
    for y in range(N):
        if lst[x][y] == 0: # 아직 방문 하지 않은 곳이면
            res += 1
            Q.append((x, y))
            cnt = 1
            lst[x][y] = res
            while Q:
                a, b = Q.pop()
                for c in d:
                    ar, br = a + c[0], b + c[1]
                    if 0 <= ar < M and 0 <= br < N and lst[ar][br] == 0:
                        lst[ar][br] = res
                        Q.append((ar, br))
                        cnt += 1

            check.append(cnt)

check.sort()
print(res)
print(*check)