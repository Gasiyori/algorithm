from sys import stdin, stdout

def dfs(graph, v, visited): # 노드, 엣지, 방문정보
    visited[v] = True # 현재 노드 방문처리
    stdout.write(str(v) + ' ') # 방문한 순서대로 출력
    
    for i in graph[v]: # 그래프를 처음부터 순회하면서
        if not visited[i]: # 방문하지 않은 그래프를 
            dfs(graph, i, visited) # 재귀호출

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

dfs(graph, 1, visited)