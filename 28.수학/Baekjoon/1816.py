import copy
import sys
sys.stdin = open('input.txt')

N = int(input())
res = 'YES'
prime = []

for i in range(N):
    S = int(input())
    lst = [True] * ((10^6)+1)

    for j in range(2, (10^6)+1):
        if lst[j]: # 소수의 배수는 소수가 아님
            for k in range(2*j, (10^6)+1, j):
                lst[k] = False

        if lst[j]:
            prime.append(j)

    for a in prime:
        if S % a == 0:
            res = 'NO'

    print(prime)
    print(res)