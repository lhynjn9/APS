import sys
sys.stdin = open('input.txt')

N, game = input().split()

N = int(N)
player = set()

for i in range(N):
    player.add(input())

if game == 'Y':
    print(len(player))
elif game == 'F':
    print(len(player) // 2)
else:
    print(len(player) // 3)