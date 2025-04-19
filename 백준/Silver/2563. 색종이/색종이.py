# 색종이 수 n
n = int(input())
# 도화지의 크기
matrix = [[0] * 100 for _ in range(100)]
for _ in range(n):
    # 색종이의 왼쪽 변과 왼쪽 도화지 사이의 거리
    # 색종이의 아랫쪽 변과 도화지 아래쪽 변 사이의 거리
    # 색종이가 도화지 밖으로 나가는 경우는 존재하지 않음
    l ,d = map(int, input().split())
    l = l-1
    d = d -1
    # 색종이의 크기는 10 * 10 으로 고정
    # 색종이를 붙일 영역
    for i in range(l, l + 10):
        for j in range(d, d + 10):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
ans = 0

for i in range(100):
    for j in range(100):
        if matrix[i][j] == 1:
            ans += 1
        
print(ans)