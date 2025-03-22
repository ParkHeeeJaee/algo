'''
예산
모든 요청이 배정가능 - 요정한 금액 그대로
불가능하면 특정한 정수 상한액 계산, 그 이상인 예산 요청에는 모두 상한액 배정
이하면 요청금액 그대로
'''
n = int(input())
requests = list(map(int, input().split()))
m = int(input())

# 이분 탐색 s 시작점, end 끝점
start = 0
end = max(requests)
answer = 0

# 이분 탐색
while start <= end:
    mid = (start + end) // 2
    total = 0

    # 배정된 예산
    for r in requests:
        if r > mid:
            total += mid
        else:
            total += r

    # 예산보다 적으면 예산을 늘린다.
    if total <= m:
        answer = mid 
        start = mid + 1
    else:
        end = mid - 1

print(answer)
