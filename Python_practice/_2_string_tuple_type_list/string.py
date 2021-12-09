#큰 따옴표는 작은 따옴표를 포함할 수 있고, 작은 따옴표는 그 반대이다.
#같은 따옴표는 백 슬래시(\)를 통해 추가 할 수 있다.

data = 'Hello world'
print(data)

data = "Don't you know \"Python\"?"
print(data)


#문자열은 인덱싱이나 슬라이싱은 가능하나 특정 인덱스 값을 변경할 수 없다.
#연결은 +를 이용하고, 문자열을 x(곱)하면 그 값만큼 문자열이 더해진다.

a = "Hello"
b = "World"

print("\n"+ a + " "+b)

a= "string"
print(a*3)

a = "ABCDEF"
print(a[2:4])

#튜플 자료형은 한번 선언된 값을 변경 불가
#리스트와 달리 소괄호()를 사용
#리스트보다 공간 효율적

print("")

a = (1,2,3,4,5,6,7,8,9)
print(a[3])
print(a[1:4])