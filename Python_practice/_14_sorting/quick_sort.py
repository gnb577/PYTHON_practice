
#퀵정렬은 기본적으로 나눠진 구역 제일 왼쪽의 pivot으로 부터
#정렬하는 시스템이다.
array = [5,7,9,0,3,1,6,2,4,8]
pivot = array[0]

def quick_sort(array,start,end):
    if start >= end:
        return
    pivot = start
    left = start +1
    right = end
    
    #left <= right는 최초 교차지점 까지 행위를 반복함
    #구역을 분할하기 위해
    while(left <= right):
        #left에서 부터 pivot이상의 값을 탐색
        while(left <= end and array[left] <= array[pivot]):
            left +=1
        #right는 역으로 pivot이하의 값을 탐색
        while(right > start and array[right] >= array[pivot]):
            right -=1
        
        #교차가 되었다면 pivot과 right를 바꿈   
        if(left> right):
            array[right],array[pivot] = array[pivot],array[right]
        else:
            array[left],array[right] = array[right],array[left]
    
    #정렬된 왼쪽 구역과 오른쪽 구역을 recursive하게 정렬
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)
        
    
quick_sort(array,0,len(array)-1)
print(array)


#파이썬 식 쉽게 퀵정렬
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort2(array):
    if len(array) <= 1:
        return array
    
    pivot= array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(array))