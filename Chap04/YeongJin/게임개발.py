n, m = map(int, input().split())
a, b, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _  in range(n)] for _ in range(m)]
visited[a][b] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(direction):
  direction -= 1
  if direction == -1:
    direction = 3
  
  return direction

x, y = a, b
result = 1
count = 0

while True:
  d = turn_left(d)
  nx = x + dx[d]
  ny = y + dy[d]
  
  if data[nx][ny] == 0 and visited[nx][ny] == 0:
    x = nx
    y = ny
    visited[x][y] = 1
    result += 1 
    count = 0
    continue
  else:
    count += 1
  
  if count == 4:
    nx = x - dx[d] 
    ny = y - dy[d]
    
    if data[nx][ny] == 1:
      break
    else:
      x = nx
      y = ny
      count = 0 
      
print(result)