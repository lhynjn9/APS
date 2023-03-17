import sys
import math
sys.stdin = open('input.txt')

A, B = map(int, input().split())

x = int((-2*A + math.sqrt(((2*A)**2) - 4 * B)) / 2)
y = int((-2*A - math.sqrt(((2*A)**2) - 4 * B)) / 2)

if x == y:
    print(x)
elif x < y:
    print(x, y)
else:
    print(y, x)