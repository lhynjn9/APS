import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    dot = sorted(list(map(int, sys.stdin.readline().split())))
    res = 0

    d = {i: True for i in dot}

    for i in range(N):
        for j in range(i+1, N):
            if (dot[j]*2 - dot[i]) in d:
                res += 1
    print(res)
