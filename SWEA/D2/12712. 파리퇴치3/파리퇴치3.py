"""
파리 잡을거임
+ 형태, x 형태 스프레이 모드가 있음
뿌려진 일부가 영역을 벗어나도 상관은 없음 <- 근데 오류나잖아 새꺄
"""

t = int(input())
for tc in range(1, t + 1):
    # n 영역의 한변, m 칸까지 분사
    n, m = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(n)]

    # + 분사
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # x 분사
    d2 = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

    max_kill = 0

    for i in range(n):
        for j in range(n):
            plus_kill = 0
            x_kill = 0

            plus_kill += matrix[i][j]
            x_kill += matrix[i][j]

            for dy, dx in d:
                for k in range(1, m):
                    ny = i + dy * k
                    nx = j + dx * k
                    if 0 <= ny < n and 0 <= nx < n:
                        plus_kill += matrix[ny][nx]

            for dy, dx in d2:
                for k in range(1, m):
                    ny = i + dy * k
                    nx = j + dx * k
                    if 0 <= ny < n and 0 <= nx < n:
                        x_kill += matrix[ny][nx]

            kill = max(plus_kill, x_kill)
            if kill > max_kill:
                max_kill = kill

    print(f"#{tc} {max_kill}")
