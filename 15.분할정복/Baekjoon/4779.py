import sys
sys.stdin = open('input.txt')

def C(arr):
    if len(arr) == 1:
        return arr
    else:
        # 빠져야할 갯수 저장
        k = len(arr) // 3
        # 중간 배열
        mid = [' '] * k

        left = C(arr[0:k])
        right = C(arr[k*2:])

        res = left + mid + right

        return res

while True:
    try:
        N = int(input())
        x = 3**N
        # 배열 만들기
        lst = ['-'] * x
        A = C(lst)
        for i in A:
            print(i, end='')
        print()
    except EOFError:
        break