# Permutation(순열)

- 서로 다른 것들 중 몇개를 뽑아서 한 줄로 나열하는 것
- 서로 다른 n개 중 r개를 택하는 순열 : nPr
- 구현 1 : 반복 구조

```python
N = 3
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j == i:
            continue
        for k in range(1, N + 1):
            if k == i or k == j:
                continue
            print(i, j, k)
```

- 구현 2 : 재귀 구조

  ```python
  arr = [1, 2, 3]
  N = len(arr)
  visit = [0] * N  # 요소의 선택 여부 저장
  order = [0] * N  # 실제 순열의 순서를 저장
  
  def perm(k, N):
      if k == N:
          print(order)
      else:
          for i in range(N):  # 첫번째 요소 선택
              if visit[i]:
                  continue
              order[k] = arr[i]
              visit[i] = 1
              perm(k + 1, N)
              visit[i] = 0
  perm(0, N)
  ```

- 구현 3 : 교환을 통한 생성(반복 구조)

  ```python
  arr = [1, 2, 3, 4]
  N = len(arr)
  
  for i in range(0, N):
      arr[0], arr[i] = arr[i], arr[0]
      for j in range(1, N):
          arr[1], arr[j] = arr[j], arr[1]
          for k in range(2, N):
              arr[2], arr[k] = arr[k], arr[2]
              print(arr)
              
              arr[2], arr[k] = arr[k], arr[2]
          arr[1], arr[j] = arr[j], arr[1]
      arr[0], arr[i] = arr[i], arr[0]
  ```

  

- 구현 4 : 교환을 통한 생성(재귀 구조)

  ```python
  arr = [1, 2, 3, 4]
  N = len(arr)
  
  def perm(k, N):
      if k == N:
          print(arr)
      else:
          for i in range(k, N):
              arr[k], arr[i] = arr[i], arr[k]
              perm(k + 1, N)
              arr[k], arr[i] = arr[i], arr[k]
  
  perm(0, N)
  ```

  
