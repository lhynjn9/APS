import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    lst = input()
    sol = cnt = 0

    for i in range(len(lst)):
        if lst[i] == '(':  # 막대기
            cnt += 1 # 막대기 개수 추가

        else:  # ')'
            if lst[i - 1] == '(':  # 레이저이므로 막대기 자르기
                cnt -= 1  # 막대기 개수 감소
                sol += cnt # 현재 있는 막대기의 개수 만큼 증가 됨: 1개의 막대기가 2번 레이저로 맞으면 2(맞은 횟수) + 1 조각이됨

            else:  # 막대기 끝
                cnt -= 1  # 막대기 개수 감소
                sol += 1

    print(f'#{tc} {sol}')