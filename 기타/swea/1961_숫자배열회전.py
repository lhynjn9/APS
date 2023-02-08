import sys
sys.stdin = open('input.txt')

def turn(N, arr):
    lst = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N-1, -1, -1):
            lst[i].append(arr[j][i])

    return lst

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    a = turn(N, arr)
    b = turn(N, a)
    c = turn(N, b)

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(a[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(b[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(c[i][j], end='')
        print()
