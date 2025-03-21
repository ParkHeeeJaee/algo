'''
1 2-7(6) 8-19(12) 20-37(18) ....
6 의 배수 형태로 계속 증가
if n-1 / 6
'''

n = int(input())

# 시작점 + 1, 끝점 + 1
# 6의 배수 형태로 육각형이 증가하고 있음.
# 1, 6*1, 6*2, 6*3, 6*4 ..... 

if n == 1:
    print(1)
else:
    cnt = 1
    max_cnt = 1
    
    while max_cnt < n:
        max_cnt += 6 * cnt
        cnt += 1
    
    print(cnt)