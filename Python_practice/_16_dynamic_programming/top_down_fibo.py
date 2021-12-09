d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    #이미 계산된 형식이면 바로 재귀함수를 사용치 않고 활용
    if d[x] != 0:
        return d[x]
    #최초 계산식인 경우 DP테이블에 넣어 사용
    d[x] = fibo(x-2)+fibo(x-1)
    return d[x]

print(fibo(99))