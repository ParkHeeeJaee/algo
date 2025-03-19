

n = int(input())
lst = [i for i in range(1, n+1)] 
# print(lst)

# lst가 1이 될때까지
while len(lst) > 1:
    k = lst[1::2] # 홀수번째 칸
    lst = k # 홀수번째 칸에 있는 수를 lst에 저장
    
print(lst[0])