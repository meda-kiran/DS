def coinChange(sum,d):
    if sum==0:
       return 0
    if sum<0:
       return 10000
    return min([coinChange(sum-d[i],d) for i in range(0,len(d))])+1

d=[2,3,5]
sum=18
print coinChange(sum,d)
