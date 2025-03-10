'''
현주는 1 ~ n 까지 상자를 가지고 이씅ㅁ
상자의 기본 숫자 0
다음 q회 동안 일정 범위의 연속하 상자를 동일한 숫자로 변경
i버째 작업에 대해, l번 상자부터 r번 상자까지 값을 i로 변경
q회 동안 위의 작업을 순서대로 한 후 n개의 상자에 적혀있는 값들을 출력
'''

t = int(input())
for tc in range(1, t+1):
    # n = 상자의 개수, q = 변경할 횟수
    n, q = map(int, input().split())
    # print(n, q)
    box = [0] * n

    # 상자의 변경시킬 상자의 번호?
    for i in range(1, q+1):

        l, r = map(int, input().split())

        # print(l, r)
        # l부터 r 까지 변경할것, 인덱스 번호로 접근해야함
        for j in range(l-1, r): # 1 ~ 3 으로 들어갔다고 가정~

            box[j] = i

    print(f'#{tc}', *box)