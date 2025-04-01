
n = int(input())

n_factorial = 1

for i in range(1, n+1):
    n_factorial *= i

n_factorial = str(n_factorial)

n = len(n_factorial)

cnt = 0
for j in range(n):
    if n_factorial[n-1-j] == '0':
        cnt += 1
    elif n_factorial[n-1-j] != '0':
        break

print(cnt)