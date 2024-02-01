# N과 M을 공백으로 입력받기
N,M = map(int, input().split())

# 얼음틀 입력받기 
array = []
for i in range(N) :
    array.append(list(map(int, input())))

# 방향값 설정
dx = [ -1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 깊이 우선 탐색
def dfs(array, s_n, s_m):
    # 해당 노드를 방문했다면
    if array[s_n][s_m] == 1: 
        return False
    # 해당 노드를 방문하지 않았다면
    else :    
        array[s_n][s_m] = 1
        for i in range(4):
            # 배열에 벗어나는 경우
            if (0 > s_n + dx[i]) or (s_n + dx[i] >= N) or (0 > s_m + dy[i]) or (s_m + dy[i] >= M):
                pass
            # 재귀적으로 함수 호출 
            else : 
                dfs(array, s_n + dx[i], s_m + dy[i])
        return True


ICE = 0

# 모든 위치에 음료수 채우기
for i in range(N):
    for j in range(M):
        if dfs(array,i,j):
            ICE += 1

print(ICE)