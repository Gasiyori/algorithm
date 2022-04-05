a = int(input()) # X사, 1리터당 A엔
b = int(input()) # Y사, 기본요금 B엔
c = int(input()) # Y사, 기본요금 상한 사용량 C
d = int(input()) # Y사, 1리터당 추가요금 D
p = int(input()) # 한달 사용 수도 양

result_a = p * a # X사 비용

if (p <= c): # 한달 사용량이 기본 상한 사용량보다 작으면
    result_b = b # Y사의 기본 요금
else:
    result_b = b + ((p - c) * d) # 기본 요금 + 초과 금액

if (result_a >= result_b): # b가 더 싸면
    print(result_b) # b 출력
else:
    print(result_a)