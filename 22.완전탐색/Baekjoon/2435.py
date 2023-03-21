import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
lst = list(map(int, input().split()))
res = -0xffffffffffffffffffff

for i in range(N-K+1):
    x = sum(lst[i:i+K])
    res = max(res, x)

print(res)