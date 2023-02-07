import sys
sys.stdin = open('input.txt')

# T = int(input())
#
# for tc in range(1, T+1):
#     case, N = input().split()
#     lst = input().split()
#
#     nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#
#     nums_dict = {}
#     cnt = [0] * 10
#
#     # 각 개수를 저장
#     for x in lst:
#         nums_dict[x] = nums_dict.get(x, 0) + 1
#
#     ans = []
#     for i in range(10):
#         for _ in range(nums_dict[nums[i]]):
#             ans.append(nums[i])
#
#     print(case, ' '.join(ans))

T = int(input())
for _ in range(1, T+1):
    tc, N = input().split()
    arr = list(input().split())
    GNS = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    arr_sorted = []
    for i in range(10):
        for gns in arr:
            if GNS[i] == gns:
                arr_sorted.append(gns)
    print(tc)
    print(*arr_sorted)
