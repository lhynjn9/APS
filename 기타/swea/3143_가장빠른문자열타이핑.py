import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    str1, str2 = input().split()
    N = len(str1)
    M = len(str2)
    i = 0
    cnt = 0 # 문자가 들어간 횟수

    while i < N:
        for j in range(M):
            # 회문이 아닌 경우 중지
            if str1[i+j] != str2[j]:
                break
        else:
            cnt += 1
            i = i + M - 1
        i+=1

    res = N - (M - 1) * cnt
    print(f'#{tc} {res}')