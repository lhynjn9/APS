import sys
sys.stdin = open('input.txt')

def sort(A, low, high):
    if low < high and cnt <= K:
        mid = (low + high) // 2

        sort(A, low, mid)
        sort(A, mid+1, high)

        merge(A, low, mid, high)

def merge(A, low, mid, high):
    global cnt, res
    temp = []
    l, h = low, mid+1

    while l <= mid and h <= high:
        if A[l] <= A[h]:
            temp.append(A[l])
            l += 1
        else:
            temp.append(A[h])
            h += 1

    while l <= mid:
        temp.append(A[l])
        l += 1
    while h <= high:
        temp.append(A[h])
        h += 1

    l, t = low, 0

    while l <= high:

        A[l] = temp[t]
        cnt += 1
        if cnt == K:
            res = A[l]
            break
        l += 1
        t += 1


N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
cnt = 0
res = -1

sort(lst, 0, N-1)

print(res)