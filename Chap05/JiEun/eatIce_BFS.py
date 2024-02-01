from collections import deque 

# N과 M을 공백으로 입력받기
N, M = map(int,(input().split()))

array = []
for i in range(N):
    array.append(list(map(int,input())))

# 방향값 설정
dx = [-1, 0, 1 ,0]
dy = [0, -1, 0, 1]  

# 넓이 우선 탐색
def bfs(s_n, s_m):
    # 해당 노드를 방문했다면
    if array[s_n][s_m] == 1 : 
        return False
    # 해당 노드를 방문하지 않았다면
    else : 
        # 큐에 방문할 노드 넣어주기 
        queue = deque([(s_n, s_m)])
        array[s_n][s_m] = 1

        # 큐에 방문할 노드가 있다면 계속 
        while queue : 
            c_n, c_m = queue.popleft()

            for i in range(4):
                # 배열에 벗어나는 경우
                if (0 > c_n + dx[i]) or (c_n + dx[i] >= N) or (0 > c_m + dy[i]) or (c_m + dy[i] >= M):
                    pass
                # 큐에 노드 넣고 방문처리
                elif not array[c_n+dx[i]][c_m+dy[i]] :
                    array[c_n+dx[i]][c_m+dy[i]] = 1
                    queue.append((c_n+dx[i], c_m+dy[i]))
    return True

ICE = 0 
# 모든 위치에 음료수 채우기
for i in range(N):
    for j in range(M):
        if bfs(i,j) :
            ICE += 1

print(ICE)