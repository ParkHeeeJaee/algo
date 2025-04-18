'''
0 빈칸 , 1 벽, 2 괴물
'''

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]

    dir = [(-1,0), (1,0), (0,-1), (0,1)]

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 2:
              
                for dy,dx in dir:
                    k = 1
                    while True:
                        ny = i + dy * k
                        nx = j + dx * k
                        if 0 <= ny < n and 0 <= nx < n:  # 맵 범위 확인
                            if matrix[ny][nx] == 0:  # 빈칸이면 3으로 표시
                                matrix[ny][nx] = 3
                            elif matrix[ny][nx] == 1:  # 벽이면 중단
                                break
                        else:
                            break
                        k += 1

    score = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                score += 1
    
    print(f'#{tc} {score}')