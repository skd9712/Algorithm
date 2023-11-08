from collections import deque
def bfs(graph, start, visited):

    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v,end=' ')
        # 아직 방문하지 않은 인접한 원소를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                # 방문처리
                visited[i] = True

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
# 1번 노드에서 시작하는 bfs
bfs(graph,1,visited)
