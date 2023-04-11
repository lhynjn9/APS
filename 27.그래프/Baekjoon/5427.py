import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs():
    while Q:
        a, b = Q.popleft()
        if visited[a][b] != "FIRE": # 불이 아니므로 벽, 상근 중 하나
            flag = visited[a][b]
        else:
            flag = "FIRE"

        for r, c in d:
            ar = a + r
            br = b + c
            if 0 <= ar < h and 0 <= br < w: # 내부에서
                if visited[ar][br] == -1 and (arr[ar][br] == "." or arr[ar][br] == "@"): # 모두가 이동 가능한 곳이면
                    if flag == "FIRE": # 지금 움직이는게 불이면
                        visited[ar][br] = flag # 불붙이기
                    else:
                        visited[ar][br] = flag + 1 # 상근이일 경우 움직인 초 저장
                    Q.append((ar, br))
            else: # 내부가 아닌 경우
                if flag != "FIRE": # 상근이 이므로
                    return flag + 1


    return "IMPOSSIBLE"


T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    fire = []
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    Q = deque()
    visited = [[-1] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                visited[i][j] = 0
                x, y = i, j
            elif arr[i][j] == '*':
                visited[i][j] = "FIRE"
                Q.append((i, j))

    Q.append((x, y))
    print(bfs())


    # 0->1 초: 불을 한번 옮기고 bfs 한번 실행 => 반복 => 반환값에 따라 탈출과 미탈출 구분