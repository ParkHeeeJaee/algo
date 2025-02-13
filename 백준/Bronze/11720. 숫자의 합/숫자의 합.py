a = int(input())
n = list(map(int, input()))
o = len(n)
sum_lst = 0
for i in range(o):
    sum_lst += n[i]

print(sum_lst)