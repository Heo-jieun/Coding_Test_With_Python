n = int(input())
count = 0

coin_type = list(map(int, input().split()))

coin_type.sort(reverse = True)

for coin in coin_type:
  count += n//coin
  n %= coin

print(count)