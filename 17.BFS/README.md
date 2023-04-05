# BFS(Breadth First Search)

- 탐색 시작 점의 <u>인접한 정점들을 먼저 모두 차례로 방문</u>한 후, 방문했던 정점을 시작점으로 하여 다시 정점들을 차례로 방문하는 방식
- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비 우선 탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용
- visited를 처리된 것을 저장한 것에서 줄 선 것으로 바꾸어 표현해봅시다
  - 내가 탐색하려는 정점의 개수만큼만 큐가 있으면 됨
  - 왜냐면 중복이 없어서 큐 사이즈 결정이 쉬워짐
- 큐에 넣기 전에 방문 표시를 많이 함, 그래야 중복이 없음



> #### BFS Algorithm

- 입력 파라미터 : 그래프 G와 탐색 시작점 v

  ```python
  def BFS(G, v): # 그래프 G, 탐색 시작점 v
      visited = [0] * (n+1) # n : 정점의 개수
      queue = []
      queue.append(v) # 시작점 v를 큐에 삽입
      
      while queue :  # 큐가 비어있지 않은 경우
          t = queue.pop(0) # 큐의 첫번째 원소를 반환
          if not visited[t] : # 만약 방문하지 않은 곳이라면
              visited[t] = True # 방문한 것으로 표시
              visit(t) # 정점 t에서 할일을 기술
          
          for i in G[t] : # t와 연결된 모든 정점에 대해
              if not visited[i] : # 방문되지 않은 곳이라면
                  queue.append(i) # 큐에 삽입
  ```


- 입력 파라미터 : 그래프 G와 탐색 시작점 v

  ```python
  def BFS(G, v, n): # 그래프 G, 탐색 시작점 v
      visited = [0] * (n+1) # n : 정점의 개수
      queue = []
      queue.append(v) # 시작점 v를 큐에 삽입
      visited[v] = 1 # 방문 표시
      
      while queue :  # 큐가 비어있지 않은 경우
          t = queue.pop(0) # 큐의 첫번째 원소를 반환
          visit(t) # 정점 t에서 할일을 기술
      
          for i in G[t] : # t와 연결된 모든 정점에 대해
              if not visited[i] : # 방문되지 않은 곳이라면
                  queue.append(i) # 큐에 삽입
                  visited[i] = visited[n] + 1 # n으로부터 1만큼 이동 = 몇번째로 방문하였는지 표시
  ```

- 거리와 경로 계산

  ```python
  def BFS(s):
      visit = [0] * (V + 1)
      D = [0] * (V + 1)  # 시작점에서 최단 거리
      P = [0] * (V + 1)  # 최단 경로 트리(부모 저장)
      Q = [s]
      D[s] = 0
      visit[s] = 1        # 시작점을 방문하고, 큐에 삽입
      while Q:            # 빈 큐가 아닐동안 반복
          v = Q.pop(0)
          for w in G[v]:  # v의 방문하지 않은 인접 정점 w을 찾는다.
              if not visit[w]:
                  Q.append(w)
                  visit[w] = 1;
                  D[w] = D[v] + 1
                  P[w] = v
  ```

- 방문 정보와 거리를 저장하는 배열을 같이 사용

  ```python
  def BFS(s):
      visit = [0] * (V + 1)
      Q = [s]
      visit[s] = 1        # 시작점을 방문하고, 큐에 삽입
      while Q:            # 빈 큐가 아닐동안 반복
          v = Q.pop(0)    # v의 방문하지 않은 인접 정점 w을 찾는다.
          for w in G[v]:
              if not visit[w]:
                  Q.append(w)
                  visit[w] = visit[v] + 1
  ```

  

> #### BFS vs DFS

- 공통점
  - 시작점에서 경로가 존재하는 모든 정점들을 방문
    - 경로 유무를 묻는 문제 -> DFS, BFS로 다 가능
    - 결합 컴포넌트를 찾는 문제
    - 최단 경로를 찾는 문제 : BFS로 해결(DFS로 해결하려면 원래 알고리즘의 수정 필요)
- 차이점
  - DFS는 출발점에서 경로가 있는 임의 정점을 처음 방문할 때, 최단으로 방문한다는 보장을 못함
  - BFS는 처음 방문할때, 항상 최단으로 방문
    - 그렇지만, 가중치가 부여된 그래프에서는 역시 안됨