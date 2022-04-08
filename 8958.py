a = []

for _ in range(int(input())):
    a.append(input())

count = 1 # 성공 횟수 카운팅

score = 0 # 점수

for x in range(len(a)): # 리스트 요소 수만큼 반복
    for y in a[x]: # 요소 구성 문자 OX에 접근
        if y == 'O': # 맞은 경우
            score = score + count # 점수에 추가
            count = count + 1 # 카운트 증가
        else: # 틀린 경우
            count = 1
    
    print(score) # 출력

    score = 0 # 초기화
    count = 1 # 초기화