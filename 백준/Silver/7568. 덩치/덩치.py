

n = int(input())

lst =[]

for _ in range(n):
    x, y = map(int, input().split())

    lst.append((x, y))
# print(lst[1][1])
    # 덩치가 큰 조건?
    # x, y가 각각 더 커야함
    # 어떻게 비교해볼까?
rank = []

for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        elif lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    rank.append(cnt+1)

print(*rank)