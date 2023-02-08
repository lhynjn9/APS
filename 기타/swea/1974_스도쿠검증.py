import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    res = 1
    x = y = z = 0

    for i in range(9):
        check1 = []
        check2 = []
        for j in range(9):
            if arr[i][j] not in check1:
                check1.append(arr[i][j])
            if arr[j][i] not in check2:
                check2.append(arr[j][i])

        if len(check1) != 9:
            res = 0
        if len(check2) != 9:
            res = 0

    for k in range(0, 9, 3):
        for l in range(0, 9, 3):
            check3 = []
            for x in range(3):
                for y in range(3):
                    if arr[k+x][l+y] not in check3:
                        check3.append(arr[k+x][l+y])

            if len(check3) != 9:
                res = 0

    print(f'#{tc} {res}')