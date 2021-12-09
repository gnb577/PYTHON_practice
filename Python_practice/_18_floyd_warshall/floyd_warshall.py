INF = int(1e9)

N,M = map(int,input().split())

#그래프 내에 distance값이 들어간다 edge값이 아니라
graph = [[INF]*(N+1) for _ in range(N+1)]

for a in range(1,N+1):
    for b in range(1,N+1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    
for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            graph[a][b] = min(graph[a][b],graph[a][k],graph[k][b])
            


        
    
    