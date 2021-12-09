
#sum은 반드시 list형태를 가져야 하지만
result = sum([1,2,3,4,5])
print(result)


#min, max는 상관 없는 듯 하다.
min_result = min([7,3,5,2])
max_result = max(7,3,5,2)
print(min_result)
print(max_result)

#string을 계산하는 함수
result = eval("(3+5)*7")
print(result)

result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4],reverse=True)
print(result)
print(reverse_result)


array = [('홍길동',50),('이순신',32),('아무개',74)]
result = sorted(array,key=lambda x: x[1],reverse=True)
print(result)


from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

#순열과 조합
data = ['A','B','C']
result = list(permutations(data,3))
print("\n",result)

result = list(combinations(data,2))
print("\n",result)


#중복순열, 같은 인자를 여러번 쓸 수 있는 경우이면서 2개의 원소
result = list(product(data,repeat=2))
print("\n",result)

#중복조합
result = list(combinations_with_replacement(data,2))
print("\n",result)



from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))
print(counter)

import math

#최소 공배수 구하기
def lcm(a,b):
    return a * b // math.gcd(a,b) # 두 값 곱한 것에 최대 공약수 나누기

a = 21
b = 14
print(math.gcd(21,14)) #최대 공약수
print(lcm(21,14)) #최소 공배수


