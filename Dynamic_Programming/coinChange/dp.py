
def coinChange(sum,d):
    table={}
    for i in range(0,sum+1):
        table[i]=99999
    table[0]=0
    for i in range(1,sum+1):
        for j in range(0,len(d)):
            if d[j]<=i and table[i-d[j]]!=99999:
                table[i]=min(table[i],table[i-d[j]])
        table[i]=table[i]+1
    print table
    return table[sum]

sum=100
d=[40,50]
print coinChange(sum,d)

sum=8
d=[2,3,5]
print coinChange(sum,d)

sum=18
d=[1,2,3,4,5]
print coinChange(sum,d)
