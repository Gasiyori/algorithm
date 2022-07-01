from sys import stdin, stdout
from collections import deque

def bfs(graph, start, visited): # 그래프, 시작지점, 방문 여부
    queue = deque([start]) # deque 라이브러리를 사용, 리스트 형태로 start를 집어넣음

    visited[start] = True # 방문 처리

    while queue: # 큐가 빌 때까지
        v = queue.popleft() # 먼저 들어온대로 처리하여 pop
        stdout.write(str(v) + ' ') # 처리되면 출력

        for i in graph[v]: # 그래프 순회
            if not visited[i]: # 방문하지 않았으면
                queue.append(i) # 큐에 삽입 (push)
                visited[i] = True # 삽입된 큐 방문처리

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)