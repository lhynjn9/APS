import sys
sys.stdin = open('input.txt')

# 특정 행에 퀸을 놓는 함수
def dfs(row):
    global N
    global res
    
    # 모든 행에 퀸을 놓았으면 멈추기
    if(row == N):
        res += 1
        return

    # 정해진 행에 특정 열에 값을 넣는 행위 반복
    for col in range(N):
        # row행, col열에 값을 넣는 경우
        arr[row] = col
        # 특정 열에 값을 넣을 수 있는지 확인해서
        # 가능하면 다음 행을 진행
        if(possible(row)):
            dfs(row+1)
    

def possible(row):
    # 행은 위에서 걸러지므로 열과 대각선만 확인하면 됨
    for i in range(row):
        # 현재 넣은 행열(row, col)과 같은
        # 열!!에 값이 있는지 확인
        if arr[row] == arr[i]:
            return False
        # 특정 열에 값이 없다면
        # 대각선을 확인하다
        # 행의차와 열의 차가 같으면 같은 대각선에 놓여있는 경우이
        elif abs(row-i) == abs(arr[row] - arr[i]):
            return False

    return True

N = int(input())
arr = [0] * (N)
res = 0
dfs(0)
print(res)