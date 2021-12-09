i = 1
result = 0

while i<=9:
    result += i
    i +=1
    
print(result)


array = [9,8,7,6,5]

for x in array:
    print(x)

result = 0
for i in range(1,10):
    result += i

print(result)

#continue, break는 아니까 pass

#정해진 range가 없으면 0~4인듯?
for i in range(5):
    if array[i] >= 7:
        print(i+1, "번 학생은 합격 입니다.",i+1)
    

