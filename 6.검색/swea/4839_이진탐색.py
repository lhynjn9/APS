import sys
sys.stdin = open('input.txt')


def Search(page, key):
    start = 1
    end = page
    cnt = 0

    while start <= end:
        middle = (start + end) // 2
        cnt += 1
        if key == middle:
            return cnt
        elif key > middle:
            start = middle + 1
        elif key < middle:
            end = middle - 1

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    l = 1

    a = Search(P, A)
    b = Search(P, B)

    if a == b:
        res = 0
    elif a < b:
        res = 'A'
    else:
        res = 'B'

    print(f'#{tc} {res}')