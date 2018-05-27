def coinChange(sum,d,cache={}):
    if sum==0:
       return 0
    if sum<0:
       return 10000
    if sum not in cache:
       cache[sum]=min([coinChange(sum-d[i],d) for i in range(0,len(d))])+1
    return cache[sum]

d=[2,3,5]
sum=18
print coinChange(sum,d)

d=[50,40]
sum=100
print coinChange(sum,d)
