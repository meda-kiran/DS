d=[[5,10,20,30],
   [35,4,25,15],
   [92,80,61,72],
   [12,16,70,2],
   [6,18,41,3]]
rd=[[-1,-1,-1,-1],
   [-1,-1,-1,-1],
   [-1,-1,-1,-1],
   [-1,-1,-1,-1],
   [-1,-1,-1,-1]]


def maxPathMain(d):
    return maxPathDp(d,rd,0,0)

def maxPathRecursion(d,i,j):
    if i==len(d) or j==len(d[0]):
        return -11111111
    if i==len(d)-1 and j==len(d[0])-1:
        return d[i][j]
    return d[i][j]+max(maxPath(d,i,j+1),maxPath(d,i+1,j))


def maxPathDp(d,rd,i,j):
    print "maxPath called with i:%s j:%s" %(i,j)
    if i==len(d) or j==len(d[0]):
        return -11111111
    if i==len(d)-1 and j==len(d[0])-1:
        rd[i][j]=d[i][j]
        return d[i][j]
    if rd[i][j]!=-1:
       print "found dp  i:%s  j%s - returning:%s" %(i,j,rd[i][j])
       return rd[i][j]
    else:
       print "not found dp  i:%s  j%s, computing it" %(i,j)
       m=d[i][j]+max(maxPathDp(d,rd,i,j+1),maxPathDp(d,rd,i+1,j))
       rd[i][j]=m
       return m

print maxPathDp(d,rd,0,0)
print rd
