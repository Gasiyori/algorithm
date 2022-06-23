from sys import stdin, stdout

k = int(stdin.readline().rstrip())

stk = []

for _ in range(k):
    num = int(stdin.readline().rstrip())
    
    if num != 0: # 0이 아니면 추가
        stk.append(num)
    else: # 0이면 스택 제거
        del stk[-1]

stdout.write(str(sum(stk)))