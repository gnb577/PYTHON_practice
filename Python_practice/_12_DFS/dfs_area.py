def dfs(x,y):
    if x<=-1 or x>= N or y <= -1 or y >= M:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

N, M = map(int,input().split())

graph= []

for i in range(N):
    graph.append(list(map(int,input())))
    
result = 0
for i in range(N):
      for j in range(M):
          
          if dfs(i,j) == True:
              result +=1
              print("result is ",i,j)
print(result)  

#왜 이렇게 되는가?
#시작점으로 부터 가능한 모든 지점을 방문함으로써 하나의 구역 생성
#그렇게 되면 최초의 점령했던 지점만 true가 되고
#다음 번에 탐색할 때는 최초 recursive했을 때는 true였던 모든 지점이
#다시 탐색할 때는 이미 방문한 구역이기 때문에 false로 취급되어
#한 구역의 최초 방문 시점만 count가 된다.


        