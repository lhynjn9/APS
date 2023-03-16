import sys
sys.stdin = open('input.txt')

N = int(input())
remain = N % 2

if remain == 1:
    print('SK')
else:
    print('CY')