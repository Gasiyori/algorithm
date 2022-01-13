# 입력 : 첫번째줄은 전체 사과 수, 두 번째 줄은 얼마나 더 많은가?
# 출력 : 많은 사과 수, 적은 사과 수

apple = int(input())
many = int(input())

# apple, many = map(int, input().split())

print(f"{(apple + many)//2}\n{(apple - many)//2}")