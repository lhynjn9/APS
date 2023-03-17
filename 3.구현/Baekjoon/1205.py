import sys
sys.stdin = open('input.txt')

N, T, P = map(int, input().split())
if N == 0:
    print(1)
else:
    lst = list(map(int, input().split()))
    x = len(lst)

    # 점수가 제일 작은 경우
    if lst[-1] >= T and N == P:
            print(-1)

    # 중간에 들어가야 하는 경우
    else:
        rank = N + 1
        for i in range(N):
            if lst[i] <= T:
                rank = i + 1
                break
        print(rank)