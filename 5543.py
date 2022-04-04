a = int(input()) # 상덕 가격
b = int(input()) # 중덕 가격
c = int(input()) # 하덕 가격
d = int(input()) # 콜라 가격
e = int(input()) # 사이다 가격

# 세트로 주문할 때 햄버거랑 음료수 고르면 50뺀 것이 세트 메뉴

cheap_burger = min(a, b, c)
cheap_drink = min(d, e)

print(cheap_burger + cheap_drink - 50)