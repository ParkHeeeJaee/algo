'''
10개의 평점
a+, a0, a-, b+ .... d0
총점 = 중간고사 35% 기말고사 45% 과제 20%
평점 = 총점이 높은 순서대로 부여
각각의 평점은 같은 비율로 부여 가능
학점을 알고싶은 k 학생의 번호
k번째 학생의 학점을 출력
'''

t = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(1, t+1):
    # n:학생수, k: 표적 학생 번호
    n, k = map(int, input().split())
    # n 명의 점수 리스트를 이차원 배열
    # scores = [list(map(int, input().split())) for _ in range(n)]


    lst = [] # 점수 리스트
    
    for i in range(1, n+1):
        m, f, hw = map(int, input().split())
        total_score = (m * 35) + (f * 45) + (hw * 20)
        lst.append([total_score, i])
        
    # print(lst)
    # sort 써서 정렬하고 점수 부여하고 해당 번호 학생 찾으면 만사 ㅇㅋ
    # 근데 학생 번호는 어떻게 찾을것인가? lst[x, y] 에서 y값을 찾기
    lst.sort(reverse=True)
    for j in range(n):
        lst[j].append(grade[j//(n//10)])
        
    # print(lst) # 중간점검~
    # k 번째 학생의 학점 찾기
    for i in range(n):
        if lst[i][1] == k:
            print(f'#{tc} {lst[i][2]}')
            break
    