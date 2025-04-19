'''
번호를 뽑음
첫번쨰 0
이후 뽑은 번호 수 만큼 앞으로 가서 줄을 선다
'''

# 학생들의 수
n = int(input())
# n 명의 학생이 뽑은 번호
lst = list(map(int, input().split()))

# 첫번째 학생은 무조건 0
# lst 의 i 번째 숫자만큼 앞으로 이동
ans_lst = []

for i in range(n):
    k = len(ans_lst)
    ans_lst.insert(k - lst[i], i + 1)

print(' '.join(map(str, ans_lst)))