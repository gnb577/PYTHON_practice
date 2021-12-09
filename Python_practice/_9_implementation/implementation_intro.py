for i in range(5):
    for j in range(5):
        print('(',i,',',j,')',end=' ')
    print()
    
    
dx = [0,-1,0,1]
dy = [1,0,-1,0]

x,y = 2,2

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx,ny)


#내 방식
N = int(input())
x,y =1,1
route = input().split()
print(route)


for i  in range(len(route)):
    if route[i] == 'R' and y != N:
        y += 1
    if route[i] == 'L' and y != 1:
        y -= 1
    if route[i] == 'U' and x != 1:
        x -= 1
    if route[i] == 'D' and x != N:
        x += 1

print("Destination : ",x,y)
    
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
moves_types = ['L','R','U','D']
        
for plan in plans:
    
    for i in range(len(moves_types)):
        if plan == moves_types[i]:
            nx = x + dx[i]
            ny = y + dx[y]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x,y = nx, ny
    
print(x,y)
        
        