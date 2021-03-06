import sys,heapq
input = sys.stdin.readline
INF = int(1e9)

N, M  = map(int,input().split())
start = int(input())
graph = [[] for i in range(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    

def heap_dijkstra():
    q = []
    heapq.heappush(q,(start,0))
    distance[start] = 0
    while q:
        now,dist = heapq.heappop(q)
        if distance[now] < dist: #처리된적이 있는 노드
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(i[0],cost))

heap_dijkstra(start)