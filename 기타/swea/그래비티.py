import sys
sys.stdin = open('input.txt')

N = int(input())
for tc in range(1, N+1):
    lst = list(map(int, input().split()))

    max_value = 0

    for i in range(len(lst)):
        # 현재 위치의 박스의 최대 높이
        H = len(lst) - i - 1
        for j in range(i+1, len(lst)):
            if lst[i] <= lst[j]:
                H -= 1

        max_value = max(H, max_value)

    print(f'#{tc} {max_value}')
