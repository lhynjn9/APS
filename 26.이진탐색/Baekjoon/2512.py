import sys
sys.stdin = open('input.txt')

N = int(input())
lst = list(map(int, input().split()))
maxP = int(input())
start, end = 0, max(lst)

# 모든 요청에 배정 가능한 경우
if sum(lst) <= maxP:
    print(max(lst))

else:
    while start <= end:
        res = 0
        mid = (start+end) // 2

        # 가능한 금액 탐색
        for i in lst:
            if i > mid:
                res += mid
            else:
                res += i

        if res <= maxP:
            start = mid + 1
        else:
            end = mid - 1

    print(end)

