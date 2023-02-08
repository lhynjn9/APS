import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    N = int(input())
    str = input()

    direction = {'^': [-1, 0], 'v': [1, 0], '>':[0, 1], '<':[0, -1]}
    flag = True

    # 전차 위치 찾기
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '^' or arr[i][j] == 'v' or arr[i][j] == '<' or arr[i][j] == '>':
                x, y = i, j
                flag = False
                break
        if flag == False:
            break

    for k in range(N):
        if str[k] == 'U':
            if 0 <= x-1 and arr[x-1][y] == '.':
                arr[x][y] = '.'
                x -= 1
            arr[x][y] = '^'
        elif str[k] == 'D':
            if x+1 < H and arr[x+1][y] == '.':
                arr[x][y] = '.'
                x += 1
            arr[x][y] = 'v'
        elif str[k] == 'L':
            if 0 <= y-1 and arr[x][y-1] == '.':
                arr[x][y] = '.'
                y -= 1
            arr[x][y] = '<'
        elif str[k] == 'R':
            if y+1 < W and arr[x][y+1] == '.':
                arr[x][y] = '.'
                y += 1
            arr[x][y] = '>'

        else:
            a = direction[arr[x][y]]
            m, n = a[0], a[1]
            p, q = x, y

            while 0 <= p+m < H and 0 <= q+n < W:
                p += m
                q += n
                if arr[p][q] == '*':
                    arr[p][q] = '.'
                    break
                elif arr[p][q] == '#':
                    break

    print(f'#{tc+1}', end=' ')
    for i in range(H):
        print(''.join(arr[i]))
