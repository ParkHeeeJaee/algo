def count_subsequences(index, current_sum):
    # 인덱스가 N에 도달한 경우
    if index == N:
        # 현재 합이 S와 같으면 1을 반환, 그렇지 않으면 0을 반환
        return 1 if current_sum == S else 0

    # 현재 숫자를 포함시키는 경우
    include = count_subsequences(index + 1, current_sum + arr[index])
    # 현재 숫자를 포함시키지 않는 경우
    exclude = count_subsequences(index + 1, current_sum)

    # 포함시키는 경우와 포함시키지 않는 경우의 합을 반환
    return include + exclude

# 입력 받기
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 인덱스 0과 합 0으로 시작
result = count_subsequences(0, 0)

# 빈 부분수열은 세지 않기 위해 S가 0일 때 결과에서 1을 빼줌
if S == 0:
    result -= 1

print(result)
