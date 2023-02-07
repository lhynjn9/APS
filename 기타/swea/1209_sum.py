import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    res = 0
    d1 = d2 = 0

    for i in range(100):
        row = col = 0
        d1 += arr[i][i]
        d2 += arr[i][99-i]
        for j in range(100):
            row += arr[i][j]
            col += arr[j][i]
        res = max(res, max(row, col))
    res = max(res, max(d1, d1))

    print(f'#{N} {res}')