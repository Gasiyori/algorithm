from sys import stdin, stdout

n = int(stdin.readline().rstrip())

count = 0 # 가방 개수

# 5kg과 3kg 봉지가 있음

while n >= 0 : # 설탕이 남아있는 동안
    
    if n % 5 == 0 :  # 설탕이 5의 배수일 때 
        count += (n // 5)  # 5kg 봉지 개수 구함
        print(count)
        break

    n = n - 3  # 설탕이 5의 배수가 아니면 설탕을 3kg봉지에 담음
    count += 1  # 3kg 봉지 +1
else : # 설탕이 음수가 되면 (나누어지지 않는 경우)
    print(-1) #-1 출력

"""
경우의 수 파악

1. 3으로 나누어지는 경우
2. 5로 나누어지는 경우
3. 3과 5로 나누어지는 경우
4. 나누어지지 않는 경우 (-1)

"""