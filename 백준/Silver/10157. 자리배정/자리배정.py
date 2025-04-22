# 방향: 상 → 우 → 하 → 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 입력 처리
C, R = map(int, input().split())
K = int(input())

# 대기번호가 좌석 수를 초과하면 0 출력
if K > R * C:
    print(0)
else:
    # 초기화
    x, y = R - 1, 0  # 시작 위치 (맨 아래 왼쪽)
    d = 0  # 방향 인덱스
    K -= 1  # K번째 좌석을 찾기 위해 0부터 시작
    visited = [[False] * C for _ in range(R)]  # 방문 여부 배열
    visited[x][y] = True

    while K > 0:
        nx = x + dx[d]
        ny = y + dy[d]

        # 경계를 벗어나거나 이미 방문한 경우 방향 전환
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
            K -= 1
            visited[nx][ny] = True
            x, y = nx, ny
        else:
            d = (d + 1) % 4  # 방향 전환

    # 결과 출력 (열, 행 순서)
    print(y + 1, R - x)