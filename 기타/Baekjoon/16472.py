import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
X = sys.stdin.readline().rstrip()

start, end = 0, 0
maxS = 0
K = len(X)
first = ''

dict = {}
while start < K and end < K:
    # 해당 값이 이미 리스트에 있는 경우
    if X[end] in dict:
        dict[X[end]] += 1
    else:
        dict[X[end]] = 1

    if len(dict) > N:
        while start <= end and len(dict) > N:
            if dict[X[start]] == 1:
                dict.pop(X[start])
            else:
                dict[X[start]] -= 1
            start += 1

    maxS = max(maxS, sum(dict.values()))
    end += 1

print(maxS)