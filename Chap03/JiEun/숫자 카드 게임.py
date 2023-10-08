# 입력 
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

mins = []
for i in range(n):
    mins.append(min(arr[i]))

print(max(mins))