import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
W = [0]
V = [0]
res = 0

for _ in range(N):
    x, y = map(int, input().split())
    W.append(x)
    V.append(y)

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(K+1):
        dp[i][j] = dp[i-1][j]
        if j - W[i] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i]]+V[i])

print(dp[N][K])