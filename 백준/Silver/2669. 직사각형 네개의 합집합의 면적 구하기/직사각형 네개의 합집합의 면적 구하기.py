''' 
사각형의 왼쪽 아래 꼭짓점의 좌표

오른쪽 오른쪽 위 꼭짓점의 좌표
'''
# 100 * 100 의 공간 0으로 이루어져 있음
matrix = [[0] * 100 for _ in range(100)]

# 각 좌푯값을 받고 계산할 것
# 직사각형은 4개임
for _ in range(4):
    lx, ly, rx, ry = map(int, input().split())

    for i in range(lx, rx):
        for j in range(ly, ry):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
ans = 0

for i in range(100):
    for j in range(100):
        if matrix[i][j] == 1:
            ans += 1

print(ans)