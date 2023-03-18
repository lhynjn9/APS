import sys
sys.stdin = open('input.txt')

lst = list(map(int, input().split()))
minN = min(lst)

while True:
    res = 0
    for i in lst:
        if minN % i == 0:
            res += 1
    if res >= 3:
        break
    minN += 1

print(minN)
