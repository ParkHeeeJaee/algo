t = int(input())
for tc in range(1, t+1):
    lst = [list(map(int, input().split())) for _ in range(9)]
    

    ans = 1
    # 스도쿠 탐색
    for i in range(9):

        row_lst = []
        col_lst = []

        for j in range(9):

            row_lst.append(lst[i][j])
            col_lst.append(lst[j][i])

        if len(set(row_lst)) != 9 or len(set(col_lst)) != 9:
            ans = 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = []
            for x in range(3):
                for y in range(3):
                    box.append(lst[i+x][j+y])

            if len(set(box)) != 9:
                ans = 0
                break

    print(f'#{tc} {ans}')
    