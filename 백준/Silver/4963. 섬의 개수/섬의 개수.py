import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    cnt = 0
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx < w and -1 < ny < h:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    q.append((nx, ny))
                    visited[ny][nx] = True
                    cnt = 1
    
    return cnt

dx = [0, 1, 1, 1, 0, -1, -1, -1, 0]
dy = [1, 1, 0, -1, -1, -1, 0, 1, 0]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == 1:
                cnt += bfs(j, i)
    
    print(cnt)