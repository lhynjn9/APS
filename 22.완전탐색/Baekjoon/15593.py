import sys
sys.stdin = open('input.txt')

N = int(input())
time = [0] * 1001
lst = []
res = 0xfffffffffff
total = 0 # 전체 시간

for i in range(N):
    A, B = map(int, input().split())
    lst.append([A, B])
    for j in range(A, B):
        if time[j] == 0:
            total += 1
        time[j] += 1

for k in range(N):
    n = 0
    for p in range(lst[k][0], lst[k][1]):
        if time[p] <= 1: # 뺄 시간
            n += 1

    res = min(res, n)

print(total - res)
