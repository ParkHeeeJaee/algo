'''
풍선 터트림 -> 상하 좌우 4방향으로 터짐
상하좌우 델타 탐색 고려

'''

t=int(input())
for tc in range(1, t+1):
    # n : 행수, m : 열수
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    # print(lst)

    # 상하좌우
    dr = [-1, 1, 0 ,0] # 상하
    dc = [0, 0, -1, 1] # 좌우

    # 파아아앙아아아앙!
    
    max_pang = 0
    for i in range(n):
        for j in range(m):
            sum_pang = lst[i][j]
            # 풍선의 값에 따라 터지는 정도가 상이함
            pang = lst[i][j]
            # 델타 탐색, 1~4 까지 돌면서 해당하는 값에 대해 적용
            for k in range(4):
                for l in range(1, pang+1):
                    # dr은 상하로만 이동, dc는 좌우로만 이동
                    nr = i + dr[k] * l
                    nc = j + dc[k] * l
                    # 범위 설정
                    if 0<=nr<n and 0<=nc<m:
                        sum_pang += lst[nr][nc]
            # 최대값을 갱신
            if sum_pang > max_pang:
                max_pang = sum_pang

    print(f'#{tc} {max_pang}')