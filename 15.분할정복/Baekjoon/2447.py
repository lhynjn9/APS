import sys
sys.stdin = open('input.txt')

def star(N):
    if N == 3:
        return ["***", "* *", "***"]

    arr = star(N//3) # 다음 것을 호출한다
    stars = []

    for i in arr:
        stars.append(i*3)

    for j in arr:
        stars.append(j+' '*(N//3)+j)

    for i in arr:
        stars.append(i*3)

    return stars

N = int(input())

res = star(N)
print('\n'.join(res))