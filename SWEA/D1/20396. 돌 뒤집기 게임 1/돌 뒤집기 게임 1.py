'''
동전 뒤집기
i 번째부터, j개의 돌을 i의 색으로
뒤집기는 가능한 돌에 대해서만 진행
'''

t = int(input())
for tc in range(1, t+1):
    # n = n개 돌의 초기 상태, i,j를 m개 줄만큼.
    n, m = map(int, input().split())
    # stnes = 돌의 상태 0과 1임
    stones = list(map(int, input().split()))
    
    # i 번째 돌, j까지 m번반복
    for _ in range(m):
        i, j = map(int, input().split())
        # i번째 인덱스로 이용할 것이기 때문에, 인덱스임을 생각해 -1
        i -= 1
        # k번만큼 반복
        k = i

        while k < i+j:
            if k >= n:
                break

            stones[k] = stones[i]
            k += 1
    
    # 언패킹
    print (f'#{tc}', *stones)