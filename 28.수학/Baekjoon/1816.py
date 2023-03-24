import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(N):
    res = 'YES'
    S = int(input())
    lst = [True] * ((10**6)+1)
    m = int((10**6)**0.5)

    # 소수 판별
    for j in range(2, m+1):
        if lst[j]:
            for k in range(2*j, (10**6)+1, j):
                lst[k] = False

    prime = [i for i in range(2, (10**6)+1) if lst[i] == True]

    for a in prime:
        if S % a == 0:
            res = 'NO'
            break

    print(res)