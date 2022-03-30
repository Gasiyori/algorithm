from sys import stdin

a, b = map(int, stdin.readline().rstrip().split())

if a > b:
    print(">")
elif a < b:
    print("<")
elif a == b:
    print("==")