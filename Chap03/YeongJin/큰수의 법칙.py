n, m, k = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort(reverse=True)

first = nums[0]
second = nums[1]

second_count = m // (k+1)
first_count = m - second_count

print(first*first_count + second*second_count)