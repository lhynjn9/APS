import sys
sys.stdin = open('input.txt')

def sosu(x, y, z):
    res = 0
    lst = [1] * (y+1)
    a = int(y**0.5)+1

    for i in range(2, a): # 범위 내 숫자 모두 검사
        if lst[i]: # 소수인 경우, 배수는 소수가 아님
            for j in range(2*i, y+1, i):
                lst[j] = 0

    prime = [i for i in range(x, y+1) if lst[i]]

    for p in prime:
        if str(z) in str(p):
            res += 1

    return res

A, B, D = map(int, input().split())

x = sosu(A, B, D)
print(x)
