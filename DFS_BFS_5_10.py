from sys import stdin, stdout

# 세로로 n개, 가로로 m개

n, m = map(int, stdin.readline().rstrip().split())

graph = []

# n개만큼 입력받아서 리스트에 넣기
for _ in range(n):
    graph.append(list(map(int, stdin.readline().rstrip())))

# dfs 수행
def dfs(x, y):
    # 범위 지정. 인덱스는 0부터
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0: # 해당 노드를 방문하지 않았으면
        graph[x][y] = 1 # 방문 처리
        
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True
    return False

result = 0
for i in range(n): # [n][m]
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

stdout.write(str(result))