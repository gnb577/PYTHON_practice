import sys
input = sys.stdin.readline
INF = int(1e9)

#노드와 간선의 개수
N,M = map(int,input().split())

#출발노드
start = int(input())

graph =[[] for i in range(N+1)]

visited = [False]*(N+1)
distance = [INF]*(N+1)

for _ in range(M):
    # a --> b까지의 비용
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    

def get_smallest_node():
    min_value = INF
    index = 0 #최단거리가 가장 짧은 노드
    for i in range(1,N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    
    distance[start] = 0
    visited[start] = True
    
    #a,b,c에서의 연장선
    #최초 시작노드로부터 나머지 애들 까지의 거리
    for j in graph[start]:
        distance[j[0]] = j[1]
        
    for i in range(N-1):
        now = get_smallest_node()
        visited[now] = True
        
        for j in graph[now]:
            cost = distance[now] + j[i]
            
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
dijkstra(start)

