# 내 풀이
n, k = map(int, input().split())

cnt = 0
while n != 1:
  if n%k == 0:
    n //= k
  else:
    n -= 1
  cnt += 1

# 모범 답안
# n, k = map(int, input().split())
# result = 0

# while True:
#   target = (n//k) * k
#   result += (n - target)
#   n = target
  
#   if n < k:
#     break
  
#   result += 1
#   n //= k
  
# result += -1
# print(result)