x = 15

if x >=  10:
    print("x >= 10")
    
if x >=  0:
    print("x >= 0")
    
if x >=  30:
    print("x >= 30")

x = 15

if x >=  20:
    print("큰 수다")
    
elif x >=  10:
    print("보통 수다")
    
else:
    print("작은 수다")



score = 85
score = 91

if score >= 70:
    print('성적이 70점 이상입니다.')
    if score >= 90:
        print('우수한 학생입니다.')
        
else:
    print('성적이 낮습니다.')
    print('분발하세요...')
    
print('프로그램 종료....')



if score >= 70:
     pass #빈자리로 두고 싶을 때 pass를 사용할 수 있음   
else:
    print('분발하세요...')
    
print('프로그램 종료....')



#기존 언어와 달리 and or 연산자를 && || 대신 가능
if True or False:
    print("or working???")
    
if True and False:
    print("and not working??>")
    
if score <=20 or score >=90:
    print("you got an amazing score")
    
    
 
#리스트 탐색 기능
a = [1,2,3,4,5]
x = 9
y = 4

if (y in a) == True:
    print('y is in a')
    
if (x not in a) == True:
    print("x is not in a")


#한줄이면 줄바꿈이 필요없음
if score >= 80: result = "success"
else: result = "Fail"

#이렇게 if와 else를 한꺼번에 활용하는 방법도 있다. 조금 어려운듯...
result = "success" if score>=80 else "fail"
print(result)

#논리식 적용이 유용, 순차 처리를 함
x = 15
if (0 < x < 20):
    print("0~20사이의 수입니다.")