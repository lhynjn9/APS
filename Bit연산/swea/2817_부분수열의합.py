import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    res = 0

    for subset in range(1<<N):
        cnt = 0
        for j in range(N):
            if subset & (1<<j):
               cnt += A[j]

        if cnt == K:
            res += 1

    print(f'#{tc} {res}')