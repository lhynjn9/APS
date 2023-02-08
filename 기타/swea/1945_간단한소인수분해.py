import sys
sys.stdin = open('input.txt')

N = int(input())

for tc in range(1, N + 1):
    num = int(input())

    lst = [2, 3, 5, 7, 11]
    cnt = [0] * 5

    for i in range(0, 5):
        while num % lst[i] == 0:
            cnt[i] += 1
            num = num // lst[i]

    print(f'#{tc}', *cnt)
