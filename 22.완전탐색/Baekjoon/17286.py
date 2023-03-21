import math
import sys

sys.stdin = open('input.txt')

x, y = map(int, input().split())
lst = []
res = 0xfffffffffffff
visit = [0] * 3

cnt = 0
for i in range(3):
    lst.append(list(map(int, input().split())))

# 기존 좌표, 이동할 좌표
def cal(a, b, c, d):
    return math.sqrt((a-c)**2+(b-d)**2)

# 반복
def find(cnt, sum, x, y):
    global res

    if cnt == 3:
        res = min(res, sum) # 최솟값 구하기
        return
    
    else:
        for i in range(3):
            if visit[i] == 0:
                visit[i] = 1
                find(cnt + 1, sum+cal(x, y, lst[i][0], lst[i][1]), lst[i][0], lst[i][1])
                visit[i] = 0

find(0, 0, x, y)
print(int(res))