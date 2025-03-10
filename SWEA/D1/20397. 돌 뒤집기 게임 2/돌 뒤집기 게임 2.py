'''
i 번째 돌을 사이에 두고 마주보는 j개의 돌
각각 같은 색이면 뒤집고
다른 색이면 그대로 둔다
주어진 범위를 벗어나면 중단
'''
t = int(input())
for tc in range(1, t+1):
    # n = 돌의 개수, m = 뒤집기 횟수
    n, m = map(int, input().split())
    stones = list(map(int, input().split()))
    
    # m번 만큼 반복
    for _ in range(m):
        # i 번째 돌, j 마주보는 돌의 갯수
        i, j = map(int, input().split())

        # 인덱스로 접근할 것
        i -= 1
        # 종료 조건 생각
        k = 1

        # k 값이 증가, k가 j와 같을 순 있으나 초과하면 안됨.
        # ex) k= 9, j=8  i기준으로 k가 1부터 1씩 증가
        # 이 경우 최댓값은 i + j 임, i+k의 값에 접근하기 때문에
        # k 가 j  보다 크면 오류
        while k <= j:
            # i-k = 0 은 가능 -> stones[0]
            # i+k = n-1 까지 가능
            if i-k < 0 or i + k == n:
                break

            elif stones[i-k] == stones[i+k]:
                stones[i-k], stones[i+k] = 1-stones[i-k], 1-stones[i+k]
            k += 1
        
    print (f'#{tc}', *stones)