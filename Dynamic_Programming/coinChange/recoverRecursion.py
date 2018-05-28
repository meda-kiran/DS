'''
problem:
Given DP table of coins combinations result, find the list of coins

TC: O(n*d)
SC: O(n)
n=size of table
d=size of list of unique coins available
'''

def recover(table,d):
    target=target=len(table)-1
    coins=[]
    while target!=0:
       tmp=target
       for i in range(0,len(d)):
           if table[target]-1 == table[target-d[i]]:
              coins.append(d[i])
              target=target-d[i]
       if tmp==target:
          break
    return coins

'''
Running 3 sample test cases
check dp.py for original tests
'''
if __name__ == "__main__":
	table=[0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4]
	d=[1,2,3,4,5]
	print "Coins:%s" %(recover(table,d)) 

	table=[0,100000,1,1,2,1,2,2,2]
	d=[2,3,5]
	print "Coins:%s" %(recover(table,d))

	table=[0, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 1, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 1, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 2, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 2, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 2]
	d=[40,50]
	print "Coins:%s" %(recover(table,d))

