import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [0] * 201
    for i in range(N):
        A, B = map(int, input().split())

        if A <= B:
            start = (A+1) // 2
            end =  (B+1) // 2
        else:
            start = (B + 1) // 2
            end = (A + 1) // 2

        for j in range(start, end+1):
            room[j] += 1

    print(f'#{tc} {max(room)}')