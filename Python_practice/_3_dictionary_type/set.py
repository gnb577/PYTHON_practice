# 집합 자료형
# 중복을 허용x
# 순서 없음
# set함수 사용

data = set([1,1,2,3,4,4,5])
print(data)

data = {1,1,2,3,4,4,5}
print(data)

# a | b 합집합
# a & b 교집합
# a - b 차집합

#원소추가
data.add(7)
print(data)

#다중 추가
data.update([8,9])
print(data)

#값 삭제
data.remove(3)
print(data)
