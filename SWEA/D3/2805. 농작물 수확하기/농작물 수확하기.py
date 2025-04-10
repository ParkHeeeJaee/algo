from collections import deque

def bfs(farm, n):

    visited = [[0] *n for _ in range(n)]

    q = deque()

    si = sj = n // 2

    q.append((si, sj))

    visited[si][sj] = 1

    profit = 0

    d = [(-1,0),(1,0),(0,-1),(0,1)]

    while q:
        i, j = q.popleft()
        profit += farm[i][j]

        for dy, dx in d:
            ny = i + dy
            nx = j + dx

            distance = abs(ny - si) + abs(nx - sj)

            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0 and distance <= n//2:
                q.append((ny, nx))
                visited[ny][nx] = 1

    return profit

t =int(input())
for tc in range(1, t+1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    result = bfs(farm, n)
    print(f'#{tc} {result}')