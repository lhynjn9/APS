# 정렬(Sort)

- 2개 이상의 자료를 특정 기준에 의해 작은 값부터 큰 값(오름차순), 혹은 반대의 순서대로(내림차순) 재배열 하는 것



> ####  버블 정렬(Bubble Sort)

- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

- 정렬 과정

  - 첫 번째 원소부터 <u>인접한</u> 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동
  - 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬됨

- **시간 복잡도 : O(n²)**

- 구현

  - 
  - 첫번째 반복
    - 구간을 줄여가며 반복
    - 버블 정렬은 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬됨
  - 두번째 반복 : 해당 구간 안에서 두 수를 비교하여 큰 수가 오른쪽에 위치하게 함
  
  ```java
  // 1
  int[] nums = {55, 7, 78, 13, 49};
  int N = nums.length;
  
  for(int i = N-1; i > 0; i--) {
      for(int j = 0; j < i; j++) {
          if(nums[j] > nums[j+1]) {
              int tmp = nums[j+1];
              nums[j] = nums[j+1];
              nums[j+1] = tmp;
          }
      }
  }
  
  // 2
  for(int i = 0; i < N; i++) {
              for(int j = 1; j < N-i; j++) {
                  if(nums[j-1] > nums[j]) {
                      int tmp = nums[j];
                      nums[j] = nums[j-1];
                      nums[j-1] = tmp;
                  }
              }
          }
  ```
  
  ```python
  def BubbleSort(a, N): # 정렬할 List a, 원소 수 N
      for i in range(N-1, 0, -1) : # 정렬될 구간 범위의 끝 위치
          for j in range(0, i): # 정렬할 원소의 인덱스
              if a[j] > a[j+1]:
                  a[j], a[j+1] = a[j+1], a[j]
  ```
  
  

> #### 선택 정렬(Selection Sort)

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

- 정렬 과정

  - 주어진 리스트 중에서 최소값/최대값과 위치를 찾음
  - 찾은 값을 리스트의 맨 앞에 위치한 값과 교환
  - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복
    - 정렬 구간의 시작이 계속 바뀌면서 구간의 길이가 줄어듦
  - 미정렬 원소가 하나 남은 상황에서는 마지막 원소가 가장 큰/작은 값을 갖게 되므로, 실행을 종료하고 선택 정렬이 완료됨

- **시간 복잡도 : O(n²)**

- 구현

  ```java
  int[] nums = {64, 25, 10, 22};
  int N = nums.length;
  
  for(int i = 0; i < N - 1; i++) {
      // 인덱스 값 저장
      int midIdx = i;
  
      for(int j = i+1; j < N; j++){
          if(nums[j] < nums[midIdx]) {
              midIdx = j;
          }
      }
      
      int tmp = nums[i];
      nums[i] = nums[midIdx];
      nums[midIdx] = tmp;
  }
  
  System.out.println(Arrays.toString(nums));
  ```

  ```python
  def selectionSort(a, N) :
      for i in range(N-1) : # 전체 리스트 탐색, 마지막 값은 비교할 필요가 없으므로 N-1
          midIdx = i # 첫번째 인덱스를 최소값으로 둠
          for j in range(i+1, N): # 두번째 값 부터 탐색
              if a[midIdx] > a[j]:
                  midIdx = j # 최소값을 가진 인덱스를 midIdx로 지정
          a[i], a[midIdx] = a[midIdx], a[i] # 기준위치 a[i]에 찾은 최소값 위치를 활용하여 a[midIdx]와 교환
  ```

  

> #### 카운팅 정렬

- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 알고리즘

- 제한 사항

  - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능
    - 각 항목의 발생 회수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문
    - 양의 정수가 적당한 범위 안에 있는 경우 유용
  - 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야함
    - 배열의 값들 중 가장 큰 값의 크기만큼 생성해야 함

- 정렬 과정

  - DATA(입력 배열)에서 각 항목들의 발생 회수를 세고, 정수 항목들로 직접 인덱스 되는 Count 배열에 저장
    - `Counts[DATA[i]] +=1`
    - 빠르게 정렬하기 위해 추가 저장공간을 사용한 것(별도의 저장공간을 만들면 처리 속도가 빠른 경우가 종종 발생)
  - Count 배열에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 Count의 원소를 조정 (=**정수 항목의 누적 정보**)
    - `Counts[i] += Count[i-1]`
  - DATA에서 맨 뒤의 값부터 Count의 인덱스(Count[DATA[i]])로 이용하여 누적 정보를 조정하고, 위의 값을 Temp(정렬된 배열)의 인덱스(Temp[Count[DATA[i]]])로 이용하여 해당 위치에 DATA의 값을 입력

- **시간 복잡도 : O(n+k)**

- 구현

  ``` python
  def ContingSort(DATA, Temp, k)
  # DATA[] : 입력 배열, 원소의 최댓값 k
  # Temp[] : 정렬된 배열
  # Count[] : 카운트 배열
  
  Count = [0] * k+1
  
  for i in range(0, len(DATA)): # 입력 배열의 원소를 인덱스로 하는 카운트 배열
      Count[A[i]] += 1
      
  for j in range(1, len(Count)): # 각 원소의 누적합을 저장
      Count[i] += Count[i-1]
      
  for l in range(len(Temp)-1, -1, -1): # 입력 배열의 값을 뒤에서부터 정렬 배열에 저장 
      Count[DATA[i]] -= 1
      Temp[Count[DATA[i]]] = DATA[i]
  ```

  - 첫번째 반복  : 원소의 개수를 세어 Count 배열을 생성
  - 두번째 반복 : 입력 배열의 원소 개수를 반영하여 Count 배열의 원소를 조정
  - 세번째 반복 : 입력 배열과  Count 배열의 정보를 이용하여 정렬된 배열을 생성



> #### 퀵 정렬

- 주어진 배열을 두개로 분할하고, 각각 정렬

- 합병 정렬과의 차이점

  - 합병 정렬은 그냥 두 부분으로 나누는 반면에, 퀵 정렬은 분할할 때, 기준 아이템(pivot) 중심으로 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킴
  - 각 부분의 정렬이 끝난 후, 합병 절렬후 합병이란 후처리가 필요하나 퀵 정렬은 필요하지 않음

- 특징

  - 최악의 시간 복잡도는 O(n²)으로, 합병 정렬에 비해 좋지 못함
  - 하지만, 퀵 정렬의 평균 복잡도는 **nlogn**임 

- **시간 복잡도 : O(n²)**

- 구현

  ```python
  def quickSort(a, begin, end):
      if begin < end : # 정렬할 영역이 남아있어야 정렬 가능
          p = partition(a, begin, end) # pivot을 만드는 알고리즘은 자유 선택
          quickSort(a, begin, p-1) # 왼쪽 영역에 대해 똑같은 작업을 재귀로 반복
          quickSort(a, p+1, end) # 오른쪽 영역에 대해 똑같은 작업을 재귀로 반복
  ```

  - partition 구현

    ```python
    def partition (a, begin, end) :
        pivot = (begin + end) // 2
        L = begin
        R = end
        while L < R : # L < R 인 경우, 두 부분이 만나지 않은 경우 계속 이동
            while (L < R and a[L] < a[pivot]): # 피봇보다 큰 부분을 만나면 멈춤
                L += 1
            while (L < R and a[R] >= a[pivot]): # 피봇보다 같거나 작은 부분을 만나면 멈춤
                R -= 1
            if L < R :
                if L == pivot : # 왼쪽 영역의 정렬이 끝난 경우
                    pivot = R
                a[L], a[R] = a[R], a[L] # 정렬
        a[pivot], a[R] = a[R], a[pivot] # L == R인 경우
        return R
    ```

    



> #### 정렬 알고리즘 비교

|  알고리즘   | 평균 수행시간 | 최악 수행시간 | 알고리즘 기법 |                       특징                       |
| :---------: | :-----------: | :-----------: | :-----------: | :----------------------------------------------: |
|  버블 정렬  |     O(n²)     |     O(n²)     |  비교와 교환  |               가장 쉬운 코딩 방법                |
| 카운팅 정렬 |    O(n+k)     |    O(n+k)     |  비교환 방식  |             n이 비교적 작을 때 가능              |
|  선택 정렬  |     O(n²)     |     O(n²)     |  비교와 교환  |         교환 횟수가 버블, 삽입보다 적음          |
|   퀵 정렬   |  O(n log n)   |     O(n²)     |   분할 정복   | 최악의 경우 O(n²) 이지만, 평균적으로는 가장 빠름 |

