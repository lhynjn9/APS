# 재귀호출

- 자기 자신을 호출하여 순환 수행 되는 것
- 재귀 호출은 반복하는 것
  - 언젠가는 함수 호출을 중단해야 됨
- 재귀 호출을 중단하기 위한 판단은 매개변수로 함
  - 반복의 횟수
  - 문제를 재귀적으로 해결하는 경우, 문제의 크기를 표현
  - 그래프의 깊이우선탐색에서는 방문하는 정점의 번호
  
- 함수에서 실행해야하는 작업의 특성에 따라 일반적인 호출방식 보다 재귀호출 방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성 가능



> #### 피보나치

- 0과 1로 시작하고 이전의 두 수 합을 다음 항으로 하는 수열

- 피보나치 수열의 i번째 값을 계산하는 함수 F의 정의

  - F0 = 0, F1 - 1
  - Fi = Fi-1 + Fi-2 for i >= 2

- 피보나치 수를 구하는 재귀함수

  ```python
  def fibo(n):
      if n < 2:
          return n
     	else:
          return fibo(n-1) + fibo(n-2)
  ```



> #### 재귀로 자료 복사

```python
def f(i, N):
    if i == N :
        print(B)
    else:
        B[i] = A[i]
        f(i+1, N)
        
A = [10, 20, 30]
B = [0] * 3
f(0, 3) #[10, 20, 30]
```



> #### 최솟값 찾기

```python
arr = [55, 17, 33, 26, 66, 78, 42, 42]

def find_min(s, e):
    if s == e:
        return arr[s]
    else: # s < e
        mid = (s + e) // 2
        l = find_min(s, mid)
        r = find_min(mid + 1, e)
        return l if l < r else r

print(find_min(0, len(arr) - 1))
```



> #### 부분집합 중 합이 k인 집합의 개수 구하기

```python
# A의 부분집합중 합이 K인 부분집합의 개수 구하기
def f(i, N, s, K):  # s: i-1원소까지 고려된 부분집합의 합
    global cnt
    if i==N:
        if s==K:
            cnt += 1
    else:
        f(i+1, N, s+A[i], K) # A[i]포함
        f(i+1, N, s, K) # A[i] 미포함

A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
K = 55
cnt = 0
f(0, N, 0, K)
print(cnt)
```



> #### 조합의 재귀적 정의

- 조합의 재귀적 정의(nCr = n-1Cr-1 + n-1Cr)
