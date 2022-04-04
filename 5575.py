from sys import stdin

# 각각의 근무시간은 시, 분, 초 3개로 나누어짐
a = list(map(int, stdin.readline().rstrip().split()))
b = list(map(int, stdin.readline().rstrip().split()))
c = list(map(int, stdin.readline().rstrip().split()))

for i in [a, b, c]:
    start = int(i[0]) * 3600 + int(i[1] * 60) + int(i[2])
    end = int(i[3]) * 3600 + int(i[4] * 60) + int(i[5])

    time = end - start

    print(time//3600, (time%3600)//60, time%60)