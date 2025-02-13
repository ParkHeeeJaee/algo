
max_num = 0
number = 0
for i in range(1,10):
    num = int(input())
    if num > max_num:
        max_num = num
        number = i

print(max_num)
print(number)