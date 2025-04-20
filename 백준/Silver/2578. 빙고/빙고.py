'''
25 칸 빙고

'''

bingo = [list(map(int, input().split())) for _ in range(5)]
cnt = 0

for _ in range(5):
    lst = list(map(int,input().split()))

    # 하나씩 0로 칠하고 1인 숫자가 이어질 경우 빙고
    for k in range(5):
        for i in range(5):
            for j in range(5):
                if bingo[i][j] == lst[k]:
                    bingo[i][j] = 0
        cnt += 1
        bing = 0

        # 하나 바꿧으니 바로 검사 실행
        # for r in range(5):

        for r in range(5):
            if sum(bingo[r]) == 0:
                bing += 1
        
        for c in range(5):
            c_sum = 0
            for r in range(5):
                c_sum += bingo[r][c]
            if c_sum == 0:
                bing += 1

        sum_l = 0
        for dia_l in range(5):
            sum_l += bingo[dia_l][dia_l]
        if sum_l == 0:
            bing += 1

        sum_r = 0
        for dia_r in range(5):
            sum_r += bingo[dia_r][4 - dia_r]
        if sum_r == 0:
            bing += 1
        
        if bing >= 3:
            print(cnt)
            exit()