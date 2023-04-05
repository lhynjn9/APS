import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
lst = list(map(int, input().split()))

res = 0
start = 0
end = 1

while end <= N and start <= end:
    s = sum(lst[start:end])

    if s == M:
        res += 1
        end += 1

    elif s < M:
        end += 1

    elif s > M:
        start += 1

print(res)