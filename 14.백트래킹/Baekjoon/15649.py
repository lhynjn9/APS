import sys
sys.stdin = open('input.txt')

def perm(k, m):
    if k == M:
        print(' '.join(map(str, out)))
        return
    for i in range(N): # 1 ~ N까지의 자연수에서 선택해야하므로
        if not visited[i]: # 아직 N을 선택 안했으므로
            visited[i] = True # 선택
            out.append(i+1) # 선택한 것의 삽입
            perm(k+1, m) # 한개를 선택했으므로 개수를 하나 더 해줌
            visited[i] = False
            out.pop()

N, M = map(int, input().split())
visited = [False] * (N+1)
out = []

# M개를 선택해야하는데
# 그 중 0개를 선택함
perm(0, M)