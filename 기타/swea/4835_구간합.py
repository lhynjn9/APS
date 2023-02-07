import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    maxCnt = 0
    minCnt = 0xfffffffff

    for i in range(0, N-M+1):
        x = 0
        for j in range(M):
            x += lst[i+j]

        if maxCnt < x:
            maxCnt = x
        if minCnt > x:
            minCnt = x

    print(f'#{tc} {maxCnt-minCnt}')
