a, b = map(int, input().split())

# a는 점수의 합, b는 점수의 차
# 득점을 먼저 한 쪽 출력

# 방정식 세워서 해결

if a < b:
    print(-1)

else:
    team1 = (a + b) // 2
    team2 = (a - b) // 2

    if (team1 + team2 == a) and (team1 - team2 == b):
        print(team1, team2)
    else:
        print(-1)