import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lst = [int(input()) for _ in range(k)]

start = 1
end = max(lst)
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = sum(x // mid for x in lst)

    if cnt >= n:
        answer = mid       # 조건 만족, 더 큰 길이 도전
        start = mid + 1
    else:
        end = mid - 1      # 조건 불만족, 길이 줄이기

print(answer)
