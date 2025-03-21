'''
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
'''
n = int(input())

lst = list(map(int, input().split()))

# 소수의 조건 나눴을때 1과 자기 자신만으로 나눠지는 수
prime_cnt = 0
for i in lst:
    if i == 1:
        continue
    
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_cnt += 1
        
print(prime_cnt)