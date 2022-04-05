t = int(input())

a, b, c = 300, 60, 10

if (t % c) != 0: # 시간을 맞추지 못하는 경우
    print(-1)

else:
    count1 = t // a
    count2 = (t % a) // b
    count3 = ((t % a) % b) // c

    print(count1, count2, count3)