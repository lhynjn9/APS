
import sys
sys.stdin = open('input.txt')
import math
H, W, N, M = map(int, input().split())

maxW = math.ceil(H/(N+1))
maxH = math.ceil(W/(M+1))

res = maxW * maxH

print(res)