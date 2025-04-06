'''
n개의 회의에 대한 회의실 사용표
각회의 i에 대해 시작 시간과 끝나는 시간이 주어져 있음.
각 회의가 겹치지 않게 하면서, 회의실을 사용할 수 있는 회의의 최대 개수
회의가 끝나자마자 바로 시작할 수 있음
'''
# 회의의 수
n = int(input())

# 회의 스케쥴
lst = []

# n+1개 줄까지 각 회의의 정보, 공백 기준으로 시작과 끝이 주어짐
for _ in range(n):
    start, end = map(int, input().split())
    lst.append((start, end))

lst.sort(key=lambda x:(x[1], x[0]))

# 회의
# now = lst[0][1]
now = 0
cnt = 0

for i in range(n):
    if lst[i][0] >= now:
        now = lst[i][1]
        cnt += 1

print(cnt)