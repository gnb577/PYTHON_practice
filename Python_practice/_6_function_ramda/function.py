def add(a,b):
    return a+b

print(add(3,7))

def add2(a,b):
    print(a , b)

#a,b이외으 값을 넣으면 오류가 나온다.
add2(b=3,a=7)


c = 0


#기존에는 전역변수를 그냥 가져다 사용했으나 python에서는 global 변수라고 명시를 하고 사용해야 한다.
def func():
    global c
    c += 1
    

for i in range(10):
    func()
    
print("c is", c)



#여러 return값을 가질 수 있다.
def operator(a,b):
    add_op = a + b
    sub_op = a - b
    mul_op = a * b
    div_op = a / b
    return add_op,sub_op,mul_op,div_op

a,b,c,d = operator(7,3)
print(a,b,c,d)

