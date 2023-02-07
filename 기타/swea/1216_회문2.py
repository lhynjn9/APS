import sys
sys.stdin = open('input.txt')

def find_palindrome(M):
    for row in range(N):
        for s in range(N - M + 1):
            e = s + M - 1
            for i in range(M // 2):
                if arr[row][s + i] != arr[row][e - i]:
                    break
            else:
                return M
            for i in range(M // 2):
                if arr[s + i][row] != arr[e - i][row]:
                    break
            else:
                return M
    return 1

N = 100
for tc in range(1, 11):
    tc_num = input()
    arr = [input() for _ in range(N)]

    ans = 0

    for M in range(100, 1, -1):
        ans = find_palindrome(M)
        if ans > 1:
            break

    print(f'#{tc} {ans}')


