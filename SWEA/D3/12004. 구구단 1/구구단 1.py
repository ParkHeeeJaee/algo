'''
정수 n
1 <= a, b <= 9
n을 a와 b의 곱으로 표현할 수 있는지 판단. 
'''

t = int(input())
for tc in range(1, t+1):
    # 정수 n
    n = int(input())
    
    # n이 a, b의 곱으로 표현 할 수 있는지 판단
    
    # n이 최대값을 넘는 경우와 최솟값보다 낮은 경우 no 출력
    # if n > 81 or n < 1:
    #     print(f'#{tc} No')
    #     break

    # a, b의 곱으로 표현될 조건?
    # 9부터 나눠볼까?
    cnt = 0
    for i in range(9, 0, -1):
        for j in range(1, 10):
            if i * j == n:
                cnt = 1
        
    if cnt == 1:
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')