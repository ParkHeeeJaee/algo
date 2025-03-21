'''
카드의 합이 21을 넘지 않는 한도 내에서 카드의 합을 최대한 크게 만드는 게임.
김정인 버전 블랙잭 - 카드에 양의 정수가 적혀져 있음.
딜러는 n장의 카드를 모두 숫자가 보이도록 바닥에 놓음
그런 후에 딜러는 숫자 m 을 선언
플레이어는 제한된 시간 안에 n장의 카드를 고름
3장의 합은 m을 넘지 않으면서 m가 최대한 가까운 수여야함.

n장의 카드에 써져 있는 숫자가 주어졌을 때,
m 을 넘지 않으면서 m에 최대한 가까운 카드 3장의 합을 출력
'''

# n 카드의 수, m 10과 같거나 크고 300,000 보다 같거나 작은 정수
n, m = map(int, input().split())

# cards 카드들
cards = list(map(int, input().split()))

# 카드가 보임으로 cards에서 세장의 카드를 뽑음.
# 정렬 시킨 후에 역순으로 카드를 뽑아볼까?

cards.sort(reverse=True)


max_sum = 0
# 3장의 카드를 뽑아야함
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            
            # 카드의 합이 m 을 넘어서는 안됨
            if cards[i] + cards[j] + cards[k] <= m:
                max_sum = max(max_sum, cards[i] + cards[j] + cards[k])
                
print(max_sum)