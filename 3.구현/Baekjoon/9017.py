import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(N):
    T = int(input())
    team = list(map(int, input().split()))
    # 1. 6명이 안되는 팀 제외
    newT = []
    for i in range(T):
        if team.count(team[i]) == 6:
            newT.append(team[i])

    dictT = {} # 팀: [점수1, 점수2, ...]
    for i in range(len(newT)):
        if dictT.get(newT[i]) == None:
            dictT[newT[i]] = [i+1]
        else:
            dictT[newT[i]].append(i+1)

    minS = 0xffffffffffffff
    minI = 201
    for key in dictT:
        x = sum(dictT[key][:4])
        if x < minS:
            minS = x
            minI = key
        elif x == minS:
            # 새로 들어온 것이 작아야 변경
            if dictT[key][4] < dictT[minI][4]:
                minI = key

    print(minI)


