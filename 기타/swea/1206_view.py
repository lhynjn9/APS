import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input()) # 건물의 개수
    lst = list(map(int, input().split())) # 건물의 높이

    count = 0
    for i in range(2, N-2):
        new_lst = [lst[i-2], lst[i-1], lst[i+1], lst[i+2]]
        mcnt = 0 # 주위에서 가장 높은 층수

        for j in range(len(new_lst)):
            if mcnt < new_lst[j]:
                mcnt = new_lst[j]

        if mcnt < lst[i]:
            count += lst[i] - mcnt

    print(f'#{tc} {count}')