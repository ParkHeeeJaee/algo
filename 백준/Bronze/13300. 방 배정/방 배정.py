'''
남 남
여 여
같은 학년
한 방의 최대인원 k
필요한 방의 최소 개수
'''

# 수학여행에 참가하는 학생 수, 한 방에 배정할 수 있는 최대 인원 수
n, k = map(int, input().split())

# n 개줄에 학생의 성별 s, 학년 y
# s 0 = 여, s = 1 남
s0_lst = []
s1_lst = []
cnt = 0
for _ in range(n):
    lst = list(map(int, input().split()))

    # s 별 분리, y 기준으로 한번 더 분리
    if lst[0] == 0:
        s0_lst.append(lst[1])
    elif lst[0] == 1:
        s1_lst.append(lst[1])

c_s0 = [0] * (7)
c_s1 = [0] * (7)

for i in range(len(s0_lst)):
    c_s0[s0_lst[i]] += 1

for i in range(len(s1_lst)):
    c_s1[s1_lst[i]] += 1

for i in range(1, 7):
    cnt += (c_s0[i] + k - 1 ) // k
    cnt += (c_s1[i] + k - 1 ) // k

print(cnt)