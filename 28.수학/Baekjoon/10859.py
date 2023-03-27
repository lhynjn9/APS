import sys
import math
sys.stdin = open('input.txt')

dic = {'0': '0', '1': '1', '2': '2', '5': '5', '6': '9', '8': '8', '9': '6'}

def isSosu(x):
    x = int(x)
    if x < 2:
        return False

    y = int(math.sqrt(x))+1
    for i in range(3, y, 2):
        if x % i == 0:
            return False
    return True

def flip(x):
    ans = ''
    a = len(x)

    for i in range(a-1, -1, -1):
        if dic.get(x[i]) == None:
            return 0
        else:
            ans += dic.get(x[i])
    return ans

N = input()
M = flip(N)

if not M:
    print('no')
else:
    x = isSosu(N)
    y = isSosu(M)
    if x and y:
        print('yes')
    else:
        print('no')
