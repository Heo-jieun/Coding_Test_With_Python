from collections import deque
# N과 M 입력받기 
N,M = map(int,input().split())

# 미로 입력받기
maze = []
for i in range(N):
    maze.append(list(map(int, input())))

# 방향값 설정
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# bfs로 미로탈출
def bfs(x, y): 
    queue = deque([(x, y)])

    while queue : 
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # maze 크기인지 확인
            if nx < 0 or nx >= N or ny< 0 or ny>= M :
                continue
            # 몬스터가 있는지 확인
            elif maze[nx][ny] == 0 :
                continue
            # 가본적 없는 곳이라면
            elif maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
        
    return maze[N-1][M-1]

answer = bfs(0,0) 
print(maze)
print(answer)
