def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v,end=' ')
    # 현재 노드와 연결된 다른 노드를 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
graph = [
    [], # 0은 그대로 냅둠
    [2,3,8], # 1번 노드
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현
visited = [False] * 9
# 1번 노드에서 시작하는 dfs
dfs(graph,1,visited)
