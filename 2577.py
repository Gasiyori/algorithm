a = int(input())
b = int(input())
c = int(input())

result = str(a * b * c)

count = [0 for _ in range(10)]

for x in result:
    if x == '0':
        count[0] = count[0] + 1
    elif x == '1':
        count[1] = count[1] + 1
    elif x == '2':
        count[2] = count[2] + 1
    elif x == '3':
        count[3] = count[3] + 1
    elif x == '4':
        count[4] = count[4] + 1
    elif x == '5':
        count[5] = count[5] + 1
    elif x == '6':
        count[6] = count[6] + 1
    elif x == '7':
        count[7] = count[7] + 1
    elif x == '8':
        count[8] = count[8] + 1
    elif x == '9':
        count[9] = count[9] + 1

for x in range(10):
    print(count[x])