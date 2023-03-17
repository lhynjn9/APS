import sys
sys.stdin = open('input.txt')

num = input()
res = 0

while True:
    res += 1
    n = str(res)
    while len(n) > 0 and len(num) > 0:
        if n[0] == num[0]:
            num = num[1:]
        n = n[1:]

    if num == '':
        print(res)
        break