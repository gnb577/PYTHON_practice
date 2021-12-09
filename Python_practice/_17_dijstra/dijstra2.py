import sys
input = sys.stdin.readline
INF = int(1e9)

N,M = map(int,input().split()) #노드의 개수랑 간선의 개수

start = int(input()) 
graph = [[] for i in range(N+1)]
visited = [False]*(N+1)
distance = [INF]*(N+1)

for _ in range(M): #간선의 값을 집어넣는 거니까 M이 맞지
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    
def get_smallest_distance():
    min_value = INF
    index = 0
    
    for i in range(1,N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra():
    distance[start] = 0
    visited[start] = True
    
    for i in range(N-1):
        now = get_smallest_distance()
        visited[now] = True
        
        for j in graph[now]:
            cost = distance[now] + j[1]
            
            if cost < distance[j[0]]:
                distance[j[0]] = cost            
    