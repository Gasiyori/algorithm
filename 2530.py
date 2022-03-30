from sys import stdin

a, b, c = map(int, stdin.readline().rstrip().split())
set = int(input())

# 시작 시간, 필요 시간 주어지면 끝나는 시간 계산
# a = 시, b = 분, c = 초, set은 설정 초

add_hour = set // 3600
add_minute = (set % 3600) // 60
add_second = set % 60

# 각 시간 단위로 쪼갬

# a가 24가 되면 0으로 변환
# b가 60이 되면 0으로 변환 + a에 + 1 or 2
# 한번에 시간이 2개씩 넘어갈수도 있으므로 캐리 사용
# b가 60이 되면 0으로 변환 + a에 + 1 or 2

carry_minute = (c + add_second) // 60 #분에 더해줄 캐리, 초에 더해진 초를 60으로 나눔
carry_hour = (b + add_minute + carry_minute) // 60 #시에 더해줄 캐리, 분에 추가 분과 캐리를 더해서 60으로 나눔

print((a + add_hour + carry_hour) % 24, (b + add_minute + carry_minute) % 60, (c + add_second) % 60) #연산에서 각 자리수에 맞게 나머지 사용