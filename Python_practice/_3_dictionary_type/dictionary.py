data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print('사과를 키로 가지는 데이터가 존재한다.\n')
    
if 'Apple' in  data:
    print('apple을 값으로 가지는 데이터가 존재한다.\n')
    
# Key값은 배열로 따지면 위치(index)와 같은 역할은 하는 것 같다.
# Data안 key 값은 탐색 할 수 있으나, value값은 탐색할 수 없다.

key_list = data.keys()
value_list = data.values()

print(key_list)
print(value_list)

for key in key_list:
    print(data[key])
    