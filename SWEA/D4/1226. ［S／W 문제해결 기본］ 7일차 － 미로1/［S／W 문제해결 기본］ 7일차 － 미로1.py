from collections import deque
t = 10
for _ in range(1, t+1):
    tc = int(input())

    maze = [list(map(int, input())) for _ in range(16)]
    n = 16
    # 상하좌우 탐색
    d = [(-1,0), (1,0), (0,-1), (0,1)]

    # 0 = 길, 1 = 벽, 2 = 출발점, 3 = 도착점
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                y, x = i, j
                break

    queue = deque()
    queue.append((y, x))
    visited = [[False] * 16 for _ in range(16)]
    visited[y][x] = True
    found = 0

    while queue:
        y, x = queue.popleft()

        for dy, dx in d:
            ny = dy + y
            nx = dx + x

            if 0 <= ny < 16 and 0 <= nx < 16:
                if maze[ny][nx] == 1:
                    continue

                elif maze[ny][nx] == 3:
                    found = 1
                    queue.clear()

                if maze[ny][nx] == 0 and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    queue.append((ny,nx))

    print(f'#{tc} {found}')
