import sys
sys.stdin = open('input.txt')

def find_palindrome():
    ret = ''
    for row in range(N): # 행
        for s in range(N - M + 1): # 행의 시작점: N개 중 M길이의 회문을 판별하기 위한 시행 N-M+1번
            e = s + M - 1 # 판별할 회문의 마지막 위치

            # row 방향 회문 판별
            for i in range(M // 2):
                if arr[row][s + i] != arr[row][e - i]:
                    break
            else:
                for i in range(M):
                    ret += arr[row][s + i]
                return ret

            # col 방향 회문 판별
            for i in range(M // 2):
                if arr[s + i][row] != arr[e - i][row]:
                    break
            else:
                for i in range(M):
                    ret += arr[s + i][row]
                return ret
    # 중간 return 을 만나지 않는 경우
    return ret

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    print(find_palindrome())

