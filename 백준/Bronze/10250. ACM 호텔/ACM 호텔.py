# 테스트 케이스 개수 입력
t = int(input())

for _ in range(t):
    # 호텔의 층 수 (H), 각 층의 방 수 (W), N번째 손님
    H, W, N = map(int, input().split())

    # 층 번호 (Y)
    floor = N % H
    if floor == 0:
        floor = H  # 나누어 떨어지면 최상층

    # 호수 번2
    # 6 12 10
    # 30 50 72호 (XX)
    room = (N // H) + 1
    if N % H == 0:
        room -= 1  # 나누어 떨어지면 호수 번호를 1 감소

    # 결과 출력 (YXX 형태)
    print(f"{floor}{room:02d}")