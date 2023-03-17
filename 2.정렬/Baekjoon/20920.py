import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
dictW = {}
for i in range(N):
    word = sys.stdin.readline().strip()

    # 단어 길이가 M 미만인 것은 제외
    if len(word) < M:
        continue
    else:
        if word in dictW:
            dictW[word] += 1
        else:
            dictW[word] = 1

dictW = sorted(dictW.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

for i in dictW:
    print(i[0])