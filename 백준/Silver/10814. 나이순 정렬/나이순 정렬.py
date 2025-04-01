lst = []

for _ in range(int(input())):
    age, name = input().split()
    age = int(age)

    lst.append((age, name))

lst.sort(key=lambda x: x[0])

for i in range(len(lst)):
    print(lst[i][0], lst[i][1])