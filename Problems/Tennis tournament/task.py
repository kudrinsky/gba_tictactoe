n = int(input())
matches = [input().split() for i in range(n)]
winners = [player[0] for player in matches if player[1] == 'win']
print(winners)
print(len(winners))
