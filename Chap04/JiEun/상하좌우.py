n = int(input())
plans = input().split()

nx, ny = 0 ,0
dir = {'L' : [0,-1], 'R' : [0,1], 'U' : [-1,0], 'D' : [1,0]}

for plan in plans : 

    nx += dir[plan][0]
    ny += dir[plan][1]
    if nx < 0 :
        nx += 1
    elif ny < 0:
        ny += 1
    elif nx > n-1 : 
        nx -= 1
    elif ny > n-1 :
        ny -= 1

print(nx+1, ny+1)