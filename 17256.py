from sys import stdin

ax, ay, az = map(int, stdin.readline().rstrip().split())
cx, cy, cz = map(int, stdin.readline().rstrip().split())

print(f"{cx - az} {cy // ay} {cz - ax}")