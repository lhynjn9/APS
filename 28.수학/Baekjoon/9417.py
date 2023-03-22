import sys
import itertools

sys.stdin = open('input.txt')

def GCD(x, y):
    res = 0
    x, y = min(x, y), max(x, y)

    for i in range(1, x+1):
        if x % i == 0 and y % i == 0 and res < i:
            res = i

    return res

N = int(input())

for i in range(N):
    res = 0
    M = list(map(int, input().split()))

    # 두 수의 쌍을 출력
    lst = list(itertools.combinations(M, 2))
    # 반복문으로 제일 큰 약수 출력
    for i in lst:
        x = GCD(i[0], i[1])
        res = max(res, x)

    print(res)