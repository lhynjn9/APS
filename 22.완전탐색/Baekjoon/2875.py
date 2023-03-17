import sys
sys.stdin = open('input.txt')

N, M, K = map(int, input().split())
res = 0

while True:
    N -= 2
    M -= 1

    if N < 0 or M < 0 or (N+M) < K:
        break

    res += 1

print(res)