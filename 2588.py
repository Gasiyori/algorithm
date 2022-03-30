a = int(input())
b = int(input())

ten = b % 10
hund = (b % 100) // 10 # 나머지로 100의 자리 필터링, 몫 연산으로 1의자리 필터링
tho = b // 100

print(a * ten)
print(a * hund)
print(a * tho)
print(a * b)
