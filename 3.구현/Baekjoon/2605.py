import sys
sys.stdin = open('input.txt')

n = int(input())
lst = list(map(int, input().split()))
res = [1]

for i in range(1, n): # 첫째 학생은 무조건 넣고 시작
    if lst[i] == 0:
        res.append(i+1)
    else:
        res.insert(i-lst[i], i+1)

print(*res)