import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

def recur(n):
    global x
    if n == 1 or n== 2:
        x += 1
        return 1
    else:
        return recur(n-1) + recur(n-2)

def dp(n):
    global y
    lst = [0] * 41
    lst[1] = 1
    lst[2] = 1
    for i in range(3, n+1):
        y += 1
        lst[i] = lst[n-1] + lst[n-2]

    return lst[n]


x, y = 0, 0

recur(N), dp(N)
print(x, y)