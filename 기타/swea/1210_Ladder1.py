import sys
sys.stdin = open('input.txt')

T = 10
for _ in range(1, T+1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if ladder[99][i] == 2:
            c = i
            break
    r = 99
    while r > 0:
        # 우회전
        if c > 0 and ladder[r][c-1]:
            while c > 0 and ladder[r][c-1]:
                c -= 1
        # 좌회전
        elif c < 99 and ladder[r][c+1]:
            while c < 99 and ladder[r][c+1]:
                c += 1
        r -= 1
    print(f'#{tc} {c}')

# 재귀
# for tc in range(1, 11):
#     N = int(input())
#     arr = [list(map(int, input().split())) for i in range(100)]
#
#     for col in range(100):
#         if arr[99][col] == 2:
#             break
#     c = col
#     r = 99
#
#     def ladder(r, c):
#         if r == 0:
#             return c
#         arr[r][c] = -100
#         if c + 1 < 100 and arr[r][c+1] == 1:
#             ret = ladder(r, c + 1)
#         elif c - 1 > 0 and arr[r][c-1] == 1:
#             ret = ladder(r, c - 1)
#         else:
#             ret = ladder(r - 1, c)
#
#         arr[r][c] = 1
#         return ret
#
#     ret = ladder(r, c)
#     print(f'#{tc} {ret}')