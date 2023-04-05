import sys
sys.stdin = open('input.txt')

def fact(x):
    if x <= 1:
        return 1

    return x * fact(x-1)

n = int(input())
print(fact(n))