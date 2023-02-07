import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    i = j = 0
    cnt = 1 # 입력할 숫자
    direction = 0 # 이동 방향
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    arr[i][j] = 1

    while cnt < N*N:
        di = i + dx[direction]
        dj = j + dy[direction]

        if 0 <= di < N and 0 <= dj < N and arr[di][dj] == 0:
            cnt += 1
            i = di
            j = dj
            arr[i][j] = cnt

        else:
            direction = (direction + 1) % 4

    print(f'#{tc}')
    for lst in arr:
        print(*lst)