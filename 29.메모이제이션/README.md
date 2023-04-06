# Memoization

- 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
- 동적 계획법의 핵심 기술



> #### 피보나치의 Memoization

- 피보나치 수를 구하는 재귀 함수는 중복 호출이 존재한다는 문제가 있음

- Momoize를 하면, 실행시간을 줄일 수 있음

  ```python
  # memo를 위한 배열을 할당하고, 모두 0으로 초기화
  # memo[0]을 0으로, memo[1]은 1로 초기화
  
  def fibo1(n) :
      global memo
      if n >= 2 and len(memo) <= n:
    # if n >= 2 and memo[n] == 0:
          memo.append(fibo(n-1) + fibo(n-2))
   	  # memo[n] = fibo(n-1) + fibo(n-2)
       return memo[n]
  
  N = 20
  memo = [0] * (N+1)
  memo[0] = 0
  memo[1] = 1
  print(fibo(N))
  ```
  
  ```python
  # 재귀
  def fibo(n):
      if n < 2:
          return n
     	else:
          return fibo(n-1) + fibo(n-2)
  ```
  
  