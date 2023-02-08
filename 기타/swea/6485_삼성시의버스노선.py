import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 노선의 수
    bus = [0] * 5001
    print(f'#{tc}', end=' ')
    for i in range(N):
        A, B = map(int, input().split())  # 거치는 정류장 좌표
        for j in range(A, B + 1):
            bus[j] += 1
    P = int(input())  # 정류장의 수
    for k in range(P):
        print(bus[int(input())], end=' ')
    print()