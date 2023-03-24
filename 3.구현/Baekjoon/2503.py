import sys
import itertools

sys.stdin = open('input.txt')

N = int(input())
data = [str(i) for i in range(1, 10)]
num = list(itertools.permutations(data, 3))

for i in range(N):
    x, st, ball = map(int, input().split())
    x = list(str(x))
    cntR = 0
    for j in range(len(num)): # 전체 순서을 확인
        s = b = 0
        j -= cntR # 숫자를 제거할 경우 자리가 변동되면서 0으로 맞춰줌
        for k in range(3): # 3자리를 확인
            if num[j][k] == x[k]: # 스트라이크는 자리와 숫자가 모두 일치
                s += 1
            elif x[k] in num[j]: # 볼은 해당 숫자를 갖고 있기만 하면 됨
                b += 1

        if(st != s) or (ball != b):
            num.remove(num[j])
            cntR += 1 # 제거한 숫자

print(len(num))

    