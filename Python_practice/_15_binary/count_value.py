N,M = list(map(int,input().split()))
array =  list(map(int,input().split()))

from bisect import bisect_left,bisect_right

left_index = bisect_left(array,M)
right_index = bisect_right(array,M)

if right_index -left_index == 0:
    print(-1)
else:
    print(right_index-left_index)