from sys import stdin, stdout

n = int(stdin.readline().rstrip())
count = 0
num = 665

while(1):
    num = num + 1 # 숫자 하나씩 증가

    if '666' in str(num): # 문자에서 666을 찾으면
        count = count + 1

    if n == count: # 입력값과 카운트가 동일할 때 종료
        stdout.write(str(num))
        break