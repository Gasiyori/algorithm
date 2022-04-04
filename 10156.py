#과자 가격K, 사려는 과자 개수 N, 가진 돈 M

k, n, m = map(int, input().split())

if (k * n - m) <= 0: # 가진 돈이 충분할 때
    print(0) # 0 출력
else:
    print(k * n - m)