#   DP(Dynamic Programming)

- 동적 계획 알고리즘
- #### **<u>점화식</u>**을 찾는 것이 핵심
- 그리디 알고리즘과 같이 **최적화 문제**를 해결하는 알고리즘
- 입력 크기가 작은 부분 문제들을 모두 해결한 후, 그 값들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘



> #### 피보나치 DP 적용

- 구현

  ```python
  # (1)
  N = 10
  fibo = [0] * (N+1)
  fibo[0] = 0
  fibo[1] = 1
  for i in range(2, N+1):
      fibo[i] = fibo[i-1] + fibo[i-2]
  
  # (2)
  def fibo2(n) : 
      f = [0, 1]
      
      for i in range(2, n + 1):
          f.append(f[i - 1] + f[i - 2])
          
      return f[n]
  
  # (3)
  def fibo1(n):
      if n < 2:
          return n
     	else:
          return fibo(n-1) + fibo(n-2)
  ```

- 구현 방식

  - recursive 방식 : fibo1 (Memoizaton)
  - iterative 방식 : fibo2
  - memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능면에서 보다 효율적
  - 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문