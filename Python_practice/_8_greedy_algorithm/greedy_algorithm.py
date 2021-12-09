#거스름 돈 구하기 greedy

n = 1260
count = 0

array = [500, 100, 50, 10]

#각 array의 코인 값마다 
for coin in array:
    count += n // coin #count = count + n // coin
    n %= coin
    print(count)

print(count)



# -1 or 나누는 수 N을 설정하여  최소기준으로 값을 출력해보자
# n = int(input())
# k = int(input())
data = list(map(int,input().split()))
n = data[0]
k = data[1]

count = 0

while(n != 1):
    if n % k == 0:
        n /= k
        count+=1
    else:
        n -= 1
        count+=1

print(count)


#가장 큰 수 연산하기
data = input()
result = int(data[0])

for i in range(1,len(data)):
    num = int(data[i])
    if num <=1 or result <=1:
        result += num
    else:
        result *= num

print(result)
