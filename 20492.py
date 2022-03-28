n = int(input())

result1 = int(n - (n * 0.22))
result2 = int((n * 0.8) + (n * 0.2 * (1 - 0.22)))

print(f"{result1} {result2}")