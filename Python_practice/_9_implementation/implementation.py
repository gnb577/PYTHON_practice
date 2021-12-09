#정수 N이 입력되면 00시 00분 00초 ~ N시 59분 59초까지
#3이 하나라도 들어가는 모든 경우의 수

# N = int(input())
# catch_num = 3

# counter = 0
# temp_counter = 0

# hour_val = 0
# min_val = 0
# sec_val = 0

# count_num = 0

    
# while(counter < 3600*(N+1)):
#     temp_counter = counter
    
#     sec_val = temp_counter % 60
#     temp_counter = (temp_counter - sec_val) / 60
    
#     min_val = temp_counter % 60
#     temp_counter = (temp_counter - min_val) / 60
    
#     hour_val = temp_counter % 24
    
#     # print(int(hour_val),int(min_val),sec_val)
#     # print(str(round(hour_val))+str(round(min_val))+str(sec_val))
#     array = str(round(hour_val))+str(round(min_val))+str(sec_val)
#     if str(catch_num) in array:
#         count_num += 1    
#     counter += 1
    
# print(count_num)
# print(counter)
    

# #체스 나이트가 움직이기
# N = int(input())
# input1 = input()
# count = 0
# x = int(ord(input1[0]))-96
# y = int(input1[1])

# dx = [1,2,2,1,-1,-2,-2,-1]
# dy = [2,1,-1,-2,-2,-1,1,2]

# tx,ty = x,y

# for i in range(N):
#     x = tx + dx[i]
#     y = ty + dy[i]
#     if x < 1 or x > 8 or y < 1 or y > 8:
#         continue
#     count += 1
# print(count)


#문자열은 정렬하고 숫자는 sum한후 문자열과 합치기
array = input()
str_array =[]
num = 0

for i in array:
    if i.isalpha():
        str_array.append(i)
    else:
        num += int(i)


#sort된 값은 return값이 none이기 때문에 별도로 
#str_array = str_array.sort()로하면 역으로 값이 지워짐
#그렇게 할거면 sorted를 사용하자
str_array.sort()
print(str_array)
str_array.append(str(num))


#join은 split함수의 반대, 나누어진 list를 하나로 합치기
print(''.join(str_array))
        