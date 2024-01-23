N,M = map(int, input().split())
# 캐릭터 초기값
A, B,d = map(int, input().split())

# 전체 맵 정보 입력받기
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))
 
direction = {0:3,1:0, 2:1, 3:2}
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 초기값
cnt = 0
maps[A][B] = 'X'
d = direction[d]
around = 0

# 움직임
while 1 :
    a = A + dx[d]
    b = B + dy[d]
    if(0 <= a < N) and (0 <= b < M ) :
        # 갈 수 있는 길인 경우
        if (maps[a][b] == 0):
            print('go')
            A = a
            B = b
            maps[A][B] = 'X'
            cnt += 1
            d = direction[d]
            around = 0
        # 갈 수 없는 길인 경우
        elif (maps[a][b] == 1) or (maps[a][b] == 'X'):
            print('block')
            d = direction[d]
            around += 1
    else : 
        break
    # 네 방향 모두 갈수 없는 경우
    if around == 4:
        print('back')
        # 뒤로 돌기
        back = direction[d]
        A = A + dx[back]
        B = B + dy[back]
        print(A,' ',B ,' ',maps[A][B])
        if maps[A][B] == 1:
            break
        cnt += 1
        around = 0
 
print(cnt)
