N = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse = True)

count = 0

for coin in coins :
    count += N // coin
    N %= coin

print(count)