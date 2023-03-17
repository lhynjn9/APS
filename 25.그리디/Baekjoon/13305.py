import sys
sys.stdin = open('input.txt')

N = int(input()) # 도시의 개수
road = list(map(int, input().split()))
price = list(map(int, input().split()))

minP = price[0] # 현재가격
res = 0

for i in range(N-1):
    # 다음 가격이 현재 가격보다 작다면
    if price[i] < minP:
        minP = price[i]

    res += minP * road[i]

print(res)