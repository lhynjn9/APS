import sys
sys.stdin = open('input.txt')

N = int(input())
res = 0

for b in range(1, 501):
    for a in range(b, 501):
        if (a ** 2) - (b ** 2) == N:
            res += 1
print(res)