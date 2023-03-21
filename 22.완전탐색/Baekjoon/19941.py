import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
D = list(input())
res = 0

for i in range(N):
    if D[i] == 'P':
        for j in range(max(i-K, 0), min(i+K+1, N)):
            if D[j] == 'H':
                D[j] = 0
                res += 1
                break
print(res)