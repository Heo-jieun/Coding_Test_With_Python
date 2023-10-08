n = int(input())
ds = input().split()

directions = {'L':(0, -1), 'R':(0, 1), 'U':(-1, 0), 'D':(1, 0)}

x, y = 1, 1
for d in ds:
  dx, dy = directions[d]
  nx = x + dx
  ny = y + dy
  if 1 <= nx <= n and 1 <= ny <= n :
    x = nx
    y = ny

print(x, y)