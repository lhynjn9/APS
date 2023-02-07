import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()
    word_dict = {"b": "d", "d": "b", "p": "q", "q": "p"}
    res = ""

    for i in range(len(word)-1, -1, -1):
        res += (word_dict[word[i]])

    print(f'#{tc} {res}')