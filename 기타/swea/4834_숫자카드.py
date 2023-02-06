import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))

    cnt = [0] * 10
    maxCnt = 0
    maxIdx = 0

    for i in num:
        cnt[i] += 1
        if cnt[i] > maxCnt:
            maxCnt = cnt[i]
            maxIdx = i
        elif cnt[i] == maxCnt and i > maxIdx:
            maxIdx = i

    print(f'#{tc} {maxIdx} {maxCnt}')
