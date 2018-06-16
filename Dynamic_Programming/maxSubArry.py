'''
Find the maximum sum over all subArrys of given array of integer
Contents can be +v, -ve and zero

example:
--------
Given list:
[904,40,523,12,-335,-385,-124,481,-31]
0    1  2   3   4    5    6   7    8

max Subarry:
[0...3]
'''

'''
Space:O(1)
Time: O(n)
'''
import itertools

def maxSubArraySum(a,size):
    #import pdb; pdb.set_trace() 
    max_so_far = -111111111
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here 
        if max_ending_here < 0:
            max_ending_here = 0  
    return max_so_far


def maxSubArraySum_2(A):
    minsum=0
    maxsum=0
    for running_sum in itertools.accumulate(A):
        print("Entering- runningSum:%s minsum:%s maxsum:%s" %(running_sum,minsum,maxsum))
        minsum=min(minsum,running_sum)
        maxsum=max(maxsum,running_sum-minsum)
        print("Exiting- runningSum:%s minsum:%s maxsum:%s" %(running_sum,minsum,maxsum))
    return maxsum



#a=[-2,-3,4,-1,-2,1,5,-3]
#print maxSubArraySum(a,len(a))
b=[904,40,523,12,-335,-385,-124,481,-31]
#print b
#print maxSubArraySum(b,len(b))
#a=[-2,-3,-4,-1,-2,-1,-5,-3]
#print maxSubArraySum(a,len(a))
print("%s" %(maxSubArraySum_2(b)))

