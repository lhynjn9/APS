import sys
sys.stdin = open('input.txt')

def cal(a, b):
    return a**2 - b**2

G = int(sys.stdin.readline())
P = 1 # 현재 몸무게
Q = 1 # 기억하고 있던 몸무게
# Q > P, Q + P <= G
start, end = 0, 0
ans = False

while P + Q <= G:
    if cal(P, Q) == G:
        print(P)
        P += 1
        ans = True
    elif cal(P, Q) > G:
        Q += 1
    elif cal(P, Q) < G:
        P += 1

if not ans:
    print(-1)

