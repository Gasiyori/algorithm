n = input()

a = {}

for x,y in zip(range(97, 97+26), range(0, 26)):
    a[chr(x)] = y # a:0, b:1... 형식

b = [-1 for _ in range(0, 26)]

# baekjoon이면 1, 0 순서, a가 나오는 곳이 2, b가 나오는 곳이 1번째 위치

for x, i in zip(n, range(len(n))): #단어 내부 순회, x는 알파벳
    if b[a[x]] == -1:
        b[a[x]] = i
        # print(a[x]) #a[x]로 문자 위치 파악

print(*b)