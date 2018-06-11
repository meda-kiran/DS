d=[[5,10,20,30],
   [35,0,-25,15],
   [92,-80,0,-72],
   [-12,16,70,2],
   [6,0,41,3]]
rd=[[-1,-1,-1,-1],
   [-1,-1,-1,-1],
   [-1,-1,-1,-1],
   [-1,-1,-1,-1],
   [-1,-1,-1,-1]]


def maxPathMain(d):
    return maxPathDp(d,rd,0,0)

def maxPathRecursion(d,i,j):
    if i==len(d) or j==len(d[0]):
        return 0
    #Above wont work because the maxSum could result in -1 and the invalid cell returning 0 could result in higher sum than max sum
    #so better put negative infinity
    if i==len(d)-1 and j==len(d[0])-1:
        return d[i][j]
    return d[i][j]+max(maxPathRecursion(d,i,j+1),maxPathRecursion(d,i+1,j))


print maxPathRecursion(d,0,0)

