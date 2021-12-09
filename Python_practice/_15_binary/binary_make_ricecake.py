#내 코드
N,M = list(map(int,input().split()))
array =  list(map(int,input().split()))

global result
result = 0

def slice_cake(array,start,end,min_sum):
    global result
    if start > end:
        return None
    
    mid = (start+end) //2
    sum = 0
    
    for i in range(N):
        if array[i] > mid:
            sum += (array[i] - mid)
            print("mid= ",mid,"sum =",sum)
    
    if sum == M:
        result = mid
        return 0
    
    if sum > M and min_sum >= sum:
        min_sum = sum
        result = mid
        print("result = ",result)
        print("sum =",sum)
    
    
    if sum > M:
        return slice_cake(array,mid+1,end,min_sum)
    else:
        return slice_cake(array,start,mid-1,min_sum)       
slice_cake(array,0,max(array)-1,1000000000)
print(result)


#답안지 
N,M = list(map(int,input().split()))
array =  list(map(int,input().split()))

start =0
end = max(array)

result = 0

while(start <= end):
    total = 0
    mid = (start+end)//2
    for x in array:
        
        if x > mid:
            total += x - mid
    
    if total < M:
        end = mid -1
    else:
        result = mid
        start = mid +1
        
print(result)

    
