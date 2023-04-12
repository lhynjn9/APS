import sys
sys.stdin = open('input.txt')

def check(target, arr):
    start = 0
    end = len(arr)-1
    mid = (start+end)//2
    near = arr[mid]

    while(start <= end):
        mid = (start+end)//2

        if arr[mid] == target:
            return target

        if arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1

        if moreApproix(arr[mid], near, target):
            near = arr[mid]


    return near;

def moreApproix(midCnt, near, target):
    if abs(midCnt-target) < abs(near - target):
        return True
    return False


A, B, C = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))
res = 0xfffffffffffffffffffffff

for i in a:
    selA = i
    selB = check(selA, b)

    selC1 = check(selA, c)
    selC2 = check(selB, c)

    max1 = max(max(selA, selB), selC1)
    min1 = min(min(selA, selB), selC1)
    score1 = max1 - min1

    max2 = max(max(selA, selB), selC2)
    min2 = min(min(selA, selB), selC2)
    score2 = max2 - min2

    res = min(res, min(score1, score2))

print(res)

