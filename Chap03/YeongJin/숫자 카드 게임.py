m, n = map(int, input().split())

result = 0
for i in range(n):
  cards = list(map(int, input().split()))
  result = max(min(cards), result)

print(result)