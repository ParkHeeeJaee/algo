# 막대기가 보이는 조건

#1. 현재 막대기보다 이후에 올 막대기가 클때.

# 보이지 않는 조건

# 1. 막대기 크기가 같음

# 2. 막대기 크기가 작음
# n개 만큼 막대기를 받음
# lst = [list(map(int, input().split())) for _ in range(n)]
import sys

n = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.read().split()))

now_s = 0
cnt = 0
# 오른쪽에서 봐야함.
for i in range(n-1,-1, -1):
    if lst[i] > now_s:
        now_s = lst[i]
        cnt += 1
    
print(cnt)