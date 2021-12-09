#계수 정렬
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0]*(max(array)+1)

#array의 각 수를 찾아 해당 값이 3이면 3에 counter를 올림
for i in range(len(array)):
    count[array[i]] +=1

#0~마지막수(9)까지    
for i in range(len(count)):
        for j in range(count[i]): #count수만큼출력
            print(i,end=' ')