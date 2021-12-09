#이진 탐색을 통한 index 찾기
def binary_search(array,target,start,end):
    if start > end: #왜 퀵정렬과 달리 >=가 아닐까?
        #퀵정렬은 end위치에 도달했음을 의미하지만
        #여기서는 모든 탐색을 맞췄는 데도 값이 없음을 의미
        return None
    mid = (start+end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)
    
N, target = list(map(int,input().split()))
array = list(map(int,input().split()))

result = binary_search(array,target,0,N-1)
if result == None:
    print('찾는 원소가 존재하지 않네요...')
else:
    print(result+1) #인덱스를 찾는 거
    

#파이썬 이진 탐색
#정렬 순서를 유지하며 해당 값을 끼워 넣을 위치를 탐색
from bisect import bisect_left,bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))

#특정 범위의 값 개수 구하기
def count_by_range(array,left,right):
    right_index = bisect_right(array,right)
    left_index = bisect_left(array,left)
    return right_index -left_index
a = [1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))    
