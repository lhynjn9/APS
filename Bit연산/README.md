# Bit 연산

- 알고리즘 문제 해결에 비트연산자를 종종 활용

  - 비트연산자는 다른 연산자들에 비해 실행 사이클이 짧음
  - 수식을 간결하게 표현 가능

- ex

  ```python
  print(10 & 7) # 2
  print(10 | 7) # 15
  
  # 홀짝 판별
  n = 5
  if n & 1:  # 홀수, /, % 연산자는 가장 느린 연산자
      print('홀수')
  else:
      print('짝수')
  
  # shift 연산자
  print(10 << 1) # 20
  print(10 << 2) # 40
  print(10 >> 1) # 5
  print(5 >> 1) # 2
  ```

  

- Binary Conting

  ```python
  arr = [1, 2, 3, 4]
  N = len(arr)  # 4
  
  # 모든 부분집합에 대응하는 정수값을 생성
  for subset in range(1 << N):
      # subset에 저장된 하위 4bit(4자리 2진수) 값을 확인
      print(subset, '==>', end=' ')
      for i in range(N):
          # subset : 부분집합의 가지 수를 비트로 표현
          # 1 << i : 특정 원소의 자릿수를 비트로 표현
          if subset & (1 << i): # & 연산을 통해 포함 여부를 확인(포함된 자릿수의 원소만 1로 표현됨)
              print(arr[i], end=' ')
      print()
  ```

  
