import heapq

#오름차순 힙정렬
def heapsort(iterable):
    
    h = []
    result = []
    
    for value in iterable:
        heapq.heappush(h,value) #아마 h라는 배열에 value push인듯
        
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)    

##내림차순 힙정렬
# def heapsort(iterable):
    
#     h = []
#     result = []
    
#     for value in iterable:
#         heapq.heappush(h,-value) #음수로 절대 가치 값을 뒤집고
        
#     for i in range(len(h)):
#         result.append(-heapq.heappop(h)) #다시 원래대로 되돌림
#     return result

# result = heapsort([1,3,5,7,9,2,4,6,8,0])
# print(result)    

