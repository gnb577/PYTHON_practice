T = int(input())

for i in range(T):
    N,M = map(int,input().split())
    lab_table = list(map(int,input().split()))
    dp = []
    index = 0
    
    for i in range(N):
        dp.append(lab_table[index:index + M])
        index += M
    
    
    
    for i in range(1,M):#열 담당, 호수담당
        for j in range(N): #행 담당, 층담당
            #현 위치로 부터 왼쪽 위, 전 위치로 부터 우측 아래
            if j == 0: left_up =0 #현 층수가 꼭대기이니가 불가능
            else: left_up = dp[j-1][i-1]
            
            if j == N-1: left_down =0
            else: left_down = dp[j+1][i-1]
            
            left = dp[j][i-1]
            
            dp[j][i]= dp[j][i]+max(left_up,left_down,left)
    result = 0
    
    for i in range(N):
        result = max(result,dp[j][M-1])

    print(result)