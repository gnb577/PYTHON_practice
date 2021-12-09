#삽입정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
        else:
            break
    print(array)


#탐색한 index까지는 정렬이 되었다고 가정하고
#현 index가 삽입될 위치를 역순으로 탐색하며 밀어냄