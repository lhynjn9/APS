import sys
sys.stdin = open('input.txt')

N = int(input())
for tc in range(1, N+1):
    K, N, M = map(int, input().split())
    battery = list(map(int, input().split()))

    bus = 0 # 버스 위치
    res = 0

    # 가장 멀리갈 수 있는 정류장에서 가장 가까운 충전소 찾기
    while bus + K < N:
        for i in range(bus + K, bus, -1):
            if i in battery:
                bus = i # 충전소 정류장
                res += 1
                break
        else:
            break

    print(f'#{tc} {res}')
