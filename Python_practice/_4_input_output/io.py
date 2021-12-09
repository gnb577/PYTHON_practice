#데이터 갯수 입력
n = int(input())

#공백을 기준으로 데이터 구분
data = list(map(int,input().split()))
data.sort(reverse=True)
print(data)

#입력 개수가 적으면 이런식으로도 가능
a,b,c = map(int, input().split())
print(a,b,c)

import sys
data = sys.stdin.readline().rstrip()
print(data)


#기본적으로 출력 후의 행위가 줄바꿈이기에 end설정을 해주면 줄바꿈이 안생김
a=1
b=2
print(a,b)
print(7,end =" ")
print(8,end=" ")

answer = 7
print("정답은 "+ str(answer)+"입니다.")

#f string
answer = 8
print(f"정답은 {answer}입니다.")