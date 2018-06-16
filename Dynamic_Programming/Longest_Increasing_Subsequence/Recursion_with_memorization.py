'''
Longest_Increasing_Subsequence
Recursion with memoization

Algorithm

In the previous approach, many recursive calls had to made again and again with the same parameters. 
This redundancy can be eliminated by storing the results obtained for a particular call in a 2-d memorization array memomemo. 
memo[i][j] represents the length of the LIS possible using nums[i] as the previous element considered to be included/not included in the LIS, with nums[j] as the current element considered to be included/not included in the LIS. 
Here, nums represents the given array.

Time complexity : O(2^n)
Size of recursion tree will be 2^n

Space complexity : O(n^2)
memo array of size n*n is used.
'''



import sys

def lisMain(num_array):
    '''
    use minint as first prev array
    '''
    memolist=[]
    for i in range(len(num_array)+1):
        memolist.append([-1]*(len(num_array)+1))
    return lis(num_array,-1,0,memolist)

def lis(num_array,prev,curr,memolist):
    '''
    recursive function to create the LIS
    '''
    if curr==len(num_array):
       return 0
    if memolist[prev+1][curr]>=0:
       return memolist[prev+1][curr]
    taken=0
    if (prev<0) or (num_array[curr]>num_array[prev]):
       taken=1+lis(num_array,curr,curr+1,memolist)
    not_taken=lis(num_array,prev,curr+1,memolist)
    memolist[prev+1][curr]=max(taken,not_taken)
    return memolist[prev+1][curr]

if __name__=='__main__':
    print lisMain([10,9,2,5,3,7,101,18])
