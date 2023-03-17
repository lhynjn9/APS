import sys
sys.stdin = open('input.txt')

N, X = map(int, input().split())
lst = list(map(int, input().split()))

if max(lst) == 0:
    print('SAD')
else:
    maxS = sum(lst[0:X])
    v = maxS
    cnt = 1

    for i in range(X, N):
        v -= lst[i-X] # 맨 앞부분 제거
        v += lst[i] # 새로운 부분 추가

        if v > maxS: # 새로운 부분이 더 크다면, 갱신
            maxS = v
            cnt = 1
        elif v == maxS:
            cnt += 1

    print(maxS)
    print(cnt)