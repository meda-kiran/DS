d=[[5,10,20,30],
   [35,4,25,15],
   [92,80,61,72],
   [12,16,70,2],
   [6,18,41,3]]
'''
d=[[4,1,17],
   [31,11,16],
   [44,2,13]]
'''

down=len(d)
right=len(d[0])
table=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
print table

for i in range(down-1,-1,-1):
    for j in range(right-1,-1,-1):
        table[i][j]=d[i][j]
        table[i][j]=table[i][j]+max(table[i+1][j],table[i][j+1])
print table

