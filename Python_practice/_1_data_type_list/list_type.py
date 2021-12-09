array = [3,4,5,2,1]
print(array)
print(array[-1])

a = [1]*10
print(a)

b = [i for i in range(10)]
print(b) #i를 원소로 사용할 건데, 그 i를 for문을 통해 0~9까지 돌리겠다. 그렇기에 앞에 i가 하나 더 붙어있는 것

c = [i for i in range(20) if i % 2 ==1] #홀수만 사용하겠다는 뜻이겠죠
d = [i*i for i in range(10)] #제곱수를 넣겠다.

#2차원 배열 초기화 하기
e = [[0] * 10 for _ in range(5)]
print(e)

#주의 사항! e = [[0]*m]*n으로 작성한 경우 0*m으로 이루어진
#각 list가 모두 같은 객체로 인식되어 변경시에 오류가 발생할 가능성이 있음

f =[[0]*10]*5
f[1][1]=3
print(f)

for _ in range(5):
    print("hello\n")
    
g = [4,3,2,1]

g.reverse()
print("원소 뒤집기: ", g)

g.insert(2,3)
print("인덱스 추가: ", g)


print("원소 뒤집기: ", g.count(3))

g.remove(1)
print("값이 1인 거 삭제: ", g)

h = [1,2,3,4,5,5,5]
remove_set ={3,5}

#remove_set에 속하지 않은 h값들만 i값으로 취급하겠다.
result = [i for i in h if i not in remove_set]
print("remove_set에 없는 list: ", result)


