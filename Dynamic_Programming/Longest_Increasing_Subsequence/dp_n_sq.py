'''
DP Approach:
TC: n**2
SC: n

logic: (check approach3)
https://leetcode.com/problems/longest-increasing-subsequence/solution/
'''

import itertools

def lis(numArray):
    dp={}
    dp[0]=1
    maxans=0
    for i in range(1,len(numArray)):
        curr_len=0
        for j in range(0,i):
            if numArray[i]>numArray[j]:
               curr_len=max(curr_len,dp[j])
        dp[i]=curr_len+1
        maxans=max(maxans,dp[i])
    return dp[len(numArray)-1]

print lis([10,9,2,5,3,7,101,18])   
