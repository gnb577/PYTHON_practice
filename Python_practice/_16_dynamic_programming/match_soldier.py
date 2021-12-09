#숫자가 오름차순 혹은 내림차순으로 정렬되어 있는 데
#그것을 방해하는 요소들을 제거하는 알고리즘

N = int(input())
array = list(map(int,input().split()))

array.reverse()

dp = [1] * N

for i in range(1,N):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i],dp[j]+1)
            
#max(dp)는 제외 안시켜도 되는 병사의 수(차순의 영향이 없는 놈들)
print(N-max(dp)) 