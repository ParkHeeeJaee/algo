'''
N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.

문자열로 입력받아서 문자열 자체를 순회하여 1의 개수를 lst 추가해서 셀까?
연속한 1을 세야함. 연속할때까지 추가하다 
'''

t = int(input())
for tc in range(1, t+1):
    # n 수열의 길이
    n = int(input())
    # n개의 0과 1로 이루어진 수열
    lst = input()
    cnt = 0
    last_cnt = []
    for i in lst:
        if i == '1':
            cnt += 1
        else:
            last_cnt.append(cnt)
            cnt = 0
    last_cnt.append(cnt)
    max_cnt = max(last_cnt)
    print(f'#{tc} {max_cnt}')