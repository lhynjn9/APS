import sys

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

a, d = map(int, sys.stdin.readline().split())
q = int(sys.stdin.readline())
k = gcd(a, d)

for i in range(q):
    x, l, r = map(int, sys.stdin.readline().split())
    start = a + (l - 1) * d  # 첫째항
    end = a + (r - 1) * d  # 마지막 항

    if x == 1:
        n = r - l + 1
        res = int(n * (start + end)//2)
        print(res)
    else:
        if l == r:
            print(start)
        else:
            print(k)