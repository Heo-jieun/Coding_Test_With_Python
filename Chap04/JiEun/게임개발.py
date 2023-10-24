N,M = map(int, input().split())
A, B,d = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

direction = {0:3,1:0, 2:1, 3:2}
dx = [-1,0,1,0]
dy = [0,-1,0,1]

cnt = 0
while cnt<5 :
    a = A + dx[d]
    b = B + dy[d]
    if(0 <= a < N) and (0 <= b < M ) :
        if (maps[a][b] != 1) and (maps[a][b] != 'X'):
            A = a
            B = b
            maps[a][b] = 'X'
            cnt += 1
            d = direction[d]
        elif (maps[a][b] != 1) and (maps[a][b] == 'X'):
            d = direction[d]
        else : 
            A = A + dx[d-1]
            B = B + dy[d-1] 
            cnt += 1
            if A==1 and B==1:
                break
    else : 
        break
         
print(cnt)
