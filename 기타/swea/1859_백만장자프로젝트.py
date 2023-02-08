import sys
sys.stdin = open('input.txt')

def trade(daily, num, sell):
    if not bool(daily):
        return sell
    else:
        max = max_idx = 0
        for i in range(num):
            if max <= daily[i]:
                max_idx = i
                max = daily[i]

        for j in range(max_idx):  # 최댓값 앞 부분 팔기
            sell += max - daily[j]

        new_daily = daily[(max_idx + 1):]
        new_num = len(new_daily)

    return trade(new_daily, new_num, sell)

T = int(input())

for tc in range(T):
    N = int(input())
    day = list(map(int, input().split()))

    print(f'#{tc + 1}', trade(day, N, 0))

