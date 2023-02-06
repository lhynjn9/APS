import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))

    for _ in range(N):
        lst = sorted(lst)
        lst[-1] = lst[-1] - 1
        lst[0] = lst[0] + 1

    res = max(lst) - min(lst)
    print(f'#{tc} {res}')
