import sys
sys.stdin = open('input.txt')

N = int(input())
grape = [0]*10001

for i in range(1, N+1):
    grape[i] = int(input())

dp = [0] *10001

dp[1] = grape[1]
dp[2] = grape[1] + grape[2]
dp[3] = max(dp[2], dp[1]+grape[3], grape[2]+grape[3])

for i in range(1, N+1):
    dp[i] = max(dp[i-1], dp[i-2]+grape[i], dp[i-3] + grape[i-1]+grape[i])


print(dp[N])