'''
2024년 2월 3일 개최 예정인 온사이트 그랜드 아레나에서는 참가자들에게
티셔츠 한 장과 펜 한 자루가 포함된 웰컴 키트를 나눠줄 예정입니다.
키트를 제작하는 업체는 다음과 같은 조건으로만 주문이 가능합니다.

티셔츠는 S, M, L, XL, XXL, 그리고 XXXL의 6가지 사이즈가 있습니다. 티셔츠는 같은 사이즈의 
$T$장 묶음으로만 주문할 수 있습니다.

펜은 한 종류로, 
$P$자루씩 묶음으로 주문하거나 한 자루씩 주문할 수 있습니다.

총 
$N$명의 참가자 중 S, M, L, XL, XXL, XXXL 사이즈의 티셔츠를 신청한 사람은 각각 
$S, M, L, XL, XXL, XXXL$명입니다. 티셔츠는 남아도 되지만 부족해서는 안 되고
신청한 사이즈대로 나눠주어야 합니다. 펜은 남거나 부족해서는 안 되고
정확히 참가자 수만큼 준비되어야 합니다.

티셔츠를 
$T$장씩 최소 몇 묶음 주문해야 하는지, 그리고 펜을 
$P$자루씩 최대 몇 묶음 주문할 수 있고, 그 때 펜을 한 자루씩 몇 개 주문하는지 구하세요.
'''

# n 참가자의 수
n = int(input())
# s,m,l,xl,xxl,xxxl 티셔츠 사이즈
lst = list(map(int, input().split()))
# t 티셔츠 묶음 수, p 펜 묶음 수
t, p = map(int, input().split())
order_t = 0
order_p = 0
order_p2 = 0
# 티셔츠는 남아도 됨, 펜은 딱 맞아야 함
for i in lst:
    if i % t != 0:
        order_t += i // t + 1
    else:
        order_t += i // t

pens = sum(lst)

if pens % p != 0:
    order_p += pens // p
    order_p2 += pens % p
else:
    order_p += pens // p
# 티셔츠를 t 장씩 최소 몇 묶음 주문해야하는지 출력
print(order_t)
# 펜을 p자루씩 몇 묶음 주문한 이후 한자루씩 몇개 주문 해야하는가?
print(f'{order_p} {order_p2}')
# print(f'{p} {order_pen * p}')
