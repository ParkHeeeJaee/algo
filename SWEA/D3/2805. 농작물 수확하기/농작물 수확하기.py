t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    lst = [list(map(int, input())) for _ in range(n)]

    mid = n // 2

    harvest = 0

    for i in range(n):
        start = abs(mid - i)
        end = n - abs(mid - i)
        for j in range(start, end):
            harvest += lst[i][j]

    print(f"#{tc} {harvest}")


"""
1
5
14054
44250
02032
51204
52212
"""
