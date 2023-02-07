import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()
    N = len(word)
    res = 0

    for i in range(N//2):
        if word[i] != word[N-1-i]:
            break
        else:
            res = 1

    print(f'#{tc} {res}')