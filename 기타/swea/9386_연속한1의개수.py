import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(T):
    N = int(input())
    arr = list(map(int, input()))

    count = 0
    max = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            if max < count:
                max = count
            count = 0

    if max < count:
        max = count

    print(f'#{tc+1} {max}')
