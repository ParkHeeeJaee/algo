'''
이차원 배열에서 풍선을 터트림
두개 터트려서 최댓값 - 최솟값 한 값이 최대 점수
풍선은 가로세로로 다 터침
'''

t = int(input())
for tc in range(1, t+1):
    # 격자의 크기
    n = int(input())
    # n개씩 숫자가 n개 만큼
    lst = [list(map(int, input().split())) for _ in range(n)]

    score = []

    for i in range(n):
        for j in range(n):
            row = 0
            col = 0
            # lst[i][j ~ n] 의 값  # lst[i~n][j~n] 의 값 # 둘을 더하고 중복되는 lst[i][j] 값을 빼준다
            for k in range(n):
                row += lst[i][k]
                col += lst[k][j]
            score.append(row + col - lst[i][j])
    
    ans = max(score) - min(score)

    print(f'#{tc} {ans}')