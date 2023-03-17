import sys
sys.stdin = open('input.txt')

candy = int(input())
res = 0

for T in range(2, candy, 2):
    Y = 1
    while True:
        N = candy - T - Y
        if N - Y >= 2:
            res += 1
            Y += 1
        else:
            break
print(res)