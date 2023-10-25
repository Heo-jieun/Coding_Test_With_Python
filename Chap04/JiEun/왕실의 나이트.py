# 값 입력받기 
location = input()
col = location[0]
row = int(location[1])-1

col_int = {'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7}
col = col_int[col]
dx = [2,2,-2,-2,1,-1,1,-1]
dy = [1,-1,1,-1,2,2,-2,-2]

cnt = 0
for i in range(len(dx)):
    if (0 <= col+dx[i] < 8) and (0 <= row+dy[i] < 8):
        cnt += 1
print(cnt)