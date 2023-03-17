import sys
sys.stdin = open('input.txt')

N = int(input())
lst = [list(input()) for _ in range(N)]
x = [(0, 1), (1, 0), (-1, 0), (0, -1)]

res = [] # 왼팔, 오른팔, 왼다리, 오른다리, 허리

# 심장 위치
for i in range(N):
    if '*' in lst[i]:
        x = i # 행
        y = lst[i].index('*') # 열
        break
print(x+2, y+1)

# 팔 길이
armL = armR = waist = legL = legR = 0

l = r = y
w = x+1

while True:
    l -= 1
    if l >= 0 and lst[x+1][l] == '*':
        armL += 1
    else:
        res.append(armL)
        break

while True:
    r += 1

    if r < N and lst[x+1][r] == '*':
        armR += 1
    else:
        res.append(armR)
        break

while True:
    w += 1

    if w < N and lst[w][y] == '*':
        waist += 1
        q = w
        p = y
    else:
        res.append(waist)
        break
        
a = b = q # 행
while True:
    a += 1
    if a < N and lst[a][p-1] == '*':
        legL += 1
    else:
        res.append(legL)
        break

while True:
    b += 1
    if b < N and lst[b][p+1] == '*':
        legR += 1
    else:
        res.append(legR)
        break

print(*res)