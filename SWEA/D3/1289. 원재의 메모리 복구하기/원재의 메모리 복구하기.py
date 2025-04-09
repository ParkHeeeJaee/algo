t = int(input())
for tc in range(1, t + 1):
    lst = list(map(int, input()))
    n = len(lst)
    # 모든 비트는 0인 상태
    now_lst = [0] * n

    cnt = 0

    for i in range(n):
        if now_lst[i] != lst[i]:
            cnt += 1

            for j in range(i, n):
                now_lst[j] = abs(now_lst[j] - 1)

    print(f"#{tc} {cnt}")
