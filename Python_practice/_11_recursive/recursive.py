# #무한 재귀 함수
# def recursive_function():
#     print('재귀함수를 호출합니다.')
#     recursive_function()
    
# recursive_function()


def recursive_function(i):
    if i == 100:
        print('재귀함수를 종료합니다...')
        return
    
    print(i, "번째 재귀함수에서", i+1 ,"번째 재귀함수를 호출합니다.")
    recursive_function(i+1)
        
recursive_function(1)

# def factorial_iterative(n):
#     result = 1
    
#     for i in range(1,n+1):
#         result = result * i
#         return result
    
N = 10
def factorial_iterative(n):
    if n <= 1:
        return 1 #이부분이 중요한 듯 생각없이 쓰는 것이 아닌 1을 return해야함
    return n * factorial_iterative(n-1)

result = factorial_iterative(10)
print(N,"!의 결과는 ",result,"입니다.")


#유클리드 호재법에 의거한 최대공약수 계산

M = 192
N = 162
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b,a % b)
    
print("M과 N의 최대 공약수는 ", gcd(M,N),"입니다.")    
