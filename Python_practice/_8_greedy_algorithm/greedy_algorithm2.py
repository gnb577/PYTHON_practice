N = int(input())
data = list(map(int,input().split()))

reverse_data=sorted(data,reverse=True)
sort_data = sorted(data)
print(sort_data)
data_len = N-1

group = 0
num = 1
temp_num = 0
max_num = 0


#내꺼
while(True):
    if(num == data_len):
        print("group count is",group)
        break
    
    max_num = max(sort_data[(temp_num):(num)]) # 11 22 233 4444
    print("temp_num is",temp_num)
    print("sort_data is",sort_data[num])
    
    if max_num == num-temp_num:
        group += 1
        temp_num = num
        print("max_num is",max_num)
    num += 1
     
     
   
    
        
   

