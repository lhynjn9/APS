import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(N):
    candy = []
    res = 0

    dum = input()
    r, c = map(int, input().split())

    for x in range(r):
        candy.append(input())

    for a in range(r):
        for b in range(c):
            if candy[a][b] == 'o':
                # 가로 사탕 확인
                if 0 <= (b-1) < c and 0 <= (b+1) < c:
                    if candy[a][b-1] == '>' and candy[a][b+1] == '<':
                        res += 1
                # 세로 사탕 확인
                if 0 <= (a-1) < r and 0 <= (a+1) < r:
                    if candy[a-1][b] == 'v' and candy[a+1][b] == '^':
                        res += 1

    print(res)
