import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    N = len(str2)
    new_str = str2.replace(str1, "")
    M = len(new_str)

    if N == M:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')


