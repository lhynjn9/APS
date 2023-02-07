import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    res = []
    lst.sort()

    while len(res) < 10:
        res.append(lst.pop(-1))
        res.append(lst.pop(0))

    print(f'#{tc}', *res)