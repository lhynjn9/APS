import sys
sys.stdin = open('input.txt')

n = int(input())
lst = list(map(int, input().split()))
x = int(input())
res = 0

lst.sort()

start = 0
end = n-1

while start < end:
    s = lst[start] + lst[end]

    if s == x:
        res += 1
        start += 1

    elif s > x:
        end -= 1

    else:
        start += 1

print(res)