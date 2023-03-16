import sys
sys.stdin = open('input.txt')

while True:
    lst = list(map(int, input().split()))
    lst.sort()
    a = lst[0]
    b = lst[1]
    c = lst[2]

    if a == 0 and b == 0 and c == 0:
        break
    elif a + b <= c:
        print('Invalid')
    elif a == b == c:
            print('Equilateral')
    elif a != b != c:
        print('Scalene')
    else:
        print('Isosceles')