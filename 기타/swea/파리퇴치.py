import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            x = 0
            for k in range(M):
                for l in range(M):
                    x += arr[i+k][j+l]

            if res < x:
                res = x

    print(f'#{tc} {res}')
