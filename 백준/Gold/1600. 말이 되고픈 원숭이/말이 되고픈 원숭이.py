'''
원숭이 쇼생크 탈출
말의 움직임 따라하기,체스판의 나이트와 같은 이동방식으로 움직임.
k번만 나이트 움직임 나머지 인접한 칸
최소 움직임으로 시작지점에서 목적지점 도착

'''
from collections import deque

# 나이트처럼 움직임
horse_dx = [-2, -1, 1, 2, 2, 1, -1, -2]
horse_dy = [1, 2, 2, 1, -1, -2, -2, -1]

# 그냥 움직임
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

k = int(input())  # 나이트 처럼 움직일 수 있는 수
w, h = map(int, input().split())  # 가로 세로

# 보드
board = [list(map(int, input().split())) for _ in range(h)]

# 방문
visit = [[[0] * w for _ in range(h)] for _ in range(k + 1)]

# 큐에 저장
q = deque()
q.append((0, 0, 0))
visit[0][0][0] = 1  # 시작 위치 방문했음.

while q:
    x, y, cnt = q.popleft()

    if x == w - 1 and y == h - 1:
        print(visit[cnt][y][x] - 1)
        exit(0)

    # 그냥 움직이기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h:
            if board[ny][nx] == 0 and visit[cnt][ny][nx] == 0:
                visit[cnt][ny][nx] = visit[cnt][y][x] + 1
                q.append((nx, ny, cnt))

    # 말처럼 이동
    if cnt < k:
        for i in range(8):
            nx = x + horse_dx[i]
            ny = y + horse_dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if board[ny][nx] == 0 and visit[cnt + 1][ny][nx] == 0:
                    visit[cnt + 1][ny][nx] = visit[cnt][y][x] + 1
                    q.append((nx, ny, cnt + 1))

# 도착못함
print(-1)