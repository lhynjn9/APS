# DFS(Depth First Search)

- 깊이우선탐색
- 시작 정점의 <u>한 방향으로 갈 수 있는 경로가 있는 곳 까지</u> 깊이 탐색하다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 반복하는 순회 방법
- **가장 마지막에 만났던 갈림길의 정점으로 되돌아와서** 다시 깊이 우선 탐색을 반복해야 하므로 후입 선출 구조의 **스택(Stack)**을 사용
- 구현 방법
  - 재귀
  - 반복
- 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요



> #### DFS Algorithm

1. 초기 상태 : 배열 visited를 False로 초기화 하고, 공백 스택 설정
2. 시작 정점 v를 결정하여 깊이 우선 탐색 시작
3. 시작 전 방문 정보를 기록해야함(정점의 수 만큼 **방문 정보를 저장**하는 배열 생성)
4. 정점 v에 인접한 정점 중에서
   1. 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문, 그리고 w를 v로 하여 다시 3.를 반복
   2. 방문하지 않은 정점이 없다면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 3.를 반복

5. 스택이 공백이 될 때 까지 2.를 반복

   ```python
   visited[], stack[] 초기화
   
   DFS(v)
   	v 방문;
       vistied[v] <- true;
       do { # 파이썬에서는 while과 if를 사용해서 do-while을 구현 가능
           if(v의 인접 정점중 방문 안한 w 찾기){
               push(v);
           	while(w) {
                   w 방문;
                   visited[w] <- true;
                   push(w);
                   v <- w;
                   v의 인접 정점 중 방문 안한 w 찾기
               }
           v <- pop(stack); # 인접 정점이 없으면
       } while(v)
   end DFS()
   ```

- DFS 반복

  ```python
  V, E = map(int, input().split())    # 정점수, 간선수
  G = [[0] * (V + 1) for _ in range(V + 1)]   # 인접 행렬
  visited = [0] * (V + 1)
  for _ in range(E):
      u, v = map(int, input().split())
      G[u][v] = G[v][u] = 1
      
  # 1) 시작 정점 v를 결정하여 방문한다.
  v = 1
  S = [0]      # 스택
  visited[v] = 1; 
  print(v, end=' ')
  
  while S:  # 3) 스택이 공백이 될 때까지 2)를 반복한다.
      
      # print(S)
      for w in range(1, V + 1):
          if G[v][w] == 1 and visited[w] == 0: # 2) 정점 v에 인접한 정점 중에서
               # 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고
              S.append(v)
              # 정점 w를 방문한다. 그리고 w를 v로 하여 다시 2)를 반복한다.
              visited[w] = 1; 
              print(w, end=' ')
              v = w
              break
      else:
          # 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서
          # 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2)를 반복한다.
          v = S.pop()
  ```

- DFS 재귀 : 인접 행렬

  ```python
  V, E = map(int, input().split())    # 정점수, 간선수
  G = [[0] * (V + 1) for _ in range(V + 1)]   # 인접 행렬
  visited = [0] * (V + 1)
  
  # 간선수만큼 입력 처리
  for _ in range(E):
      u, v = map(int, input().split())
      G[u][v] = G[v][u] = 1
  
  def dfs(v):
      visited[v] = 1; 
      print(v, end=' ')
      for w in range(1, V + 1):
          if G[v][w] == 1 and not visited[w]:
              dfs(w)
  
  dfs(1)
  ```

- DFS 재귀 : 인접 리스트

  ```python
  G = [[] for _ in range(V + 1)]   # 인접 행렬
  visited = [0] * (V + 1) # 정점수 만큼 방문정보 저장하는 배열
  # 간선수만큼 입력 처리
  for _ in range(E):
      u, v = map(int, input().split())
      G[u].append(v)
      G[v].append(u)
  
  def dfs(v): # v = 방문할 정점 번호
      visited[v] = 1 # v를 방문한다
      print(v, end=' ')
      # v의 인접 정점을 w를 찾는다.
      for w in G[v]:
          if not visited[w]:
              dfs(w)
  dfs(1)
  ```

- 그래프 경로 문제

  - 반환값을 이용한 탐색 중단

    ```python
    def DFS(v):  # 현재 방문하는 정점 번호
        visited[v] = 1;
        if v == e:
            return 1
    
        for w in G[v]:
            if not visited[w]:
                if DFS(w):
                    return 1
        return 0
    ```

  - 반환값을 모아서 처리하기

    ```python
    def DFS(v):  # 현재 방문하는 정점 번호
        visited[v] = 1;
        if v == e:
            return 1
    
        ret = 0
        for w in G[v]:
            if not visited[w]:
                ret += DFS(w)   
    
        return ret
    ```


  
