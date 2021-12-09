# 창고를 털 예정이다.
# 하지만 창고를 털 때 반드시 한 칸이상을 띄운 후 창고를
# 털어야 한다.
# 최대(최적)의 해를 구하시오.

N = int(input())

array = list(map(int,input().split()))

d = [0]* 100

#바텀업 형식으로 진행, 차례로 하겠음
d[0] = array[0]
d[1] = max(array[0],array[1])
for i in range(2,N):
    d[i] = max(d[i-1],d[i-2]+array[i])

print(d[N-1])