m, k = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()

# m = 8 
# k = 3
# arr = [2,4,5,4,6]

km = k
answer = 0
for i in range(m) :
    if km > 0 : 
        answer += max(arr)
        km -= 1
    elif km == 0 : 
        d = arr.pop(arr.index(max(arr)))
        answer += max(arr)
        arr.append(d)
        km = k
print(answer)