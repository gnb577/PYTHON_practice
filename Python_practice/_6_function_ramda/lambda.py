def add(a,b):
    return a+b

#함수를 한 줄로 적는 lambda method
print((lambda a,b: a+b)(3,7))

array = [('홍길동',50),('이순신',32),('아무개',74)]
def my_key(x):
    print(x[1])
    return x[1]


#결국 lambda (변수) : (return)의 관계가 되는 거네
#key는 정렬 기준인데, 주어진 값에 대해서 2번째 원소를 택하겠다는 뜻
#array값을 my_key한테 넘겨주기 때문에 별도의 list없이도 함수가 수행되는듯
print(sorted(array,key=my_key))
print(sorted(array,key=lambda x: x[1]))


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

#이 경우 위 lambda식과 달리 직접 값을 주지 않기에 추가로 list를 변수로 집어넣은 듯
result = map(lambda a,b: a+b, list1,list2)
print(list(result))

#amp을 사용하는 이유는 list에서 데이터를 추출하는 불편함을 줄일려고
