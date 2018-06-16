'''
Longest_Increasing_Subsequence
Brute Force Approach

Algorithm

The simplest approach is to try to find all increasing subsequences and then returning the maximum length of longest increasing subsequence. In order to do this, we make use of a recursive function lengthofLISlengthofLIS which returns the length of the LIS possible from the current element(corresponding to curposcurpos) onwards(including the current element). Inside each function call, we consider two cases:

The current element is larger than the previous element included in the LIS. In this case, we can include the current element in the LIS. Thus, we find out the length of the LIS obtained by including it. Further, we also find out the length of LIS possible by not including the current element in the LIS. The value returned by the current function call is, thus, the maximum out of the two lengths.

The current element is smaller than the previous element included in the LIS. In this case, we can't include the current element in the LIS. Thus, we find out only the length of the LIS possible by not including the current element in the LIS, which is returned by the current function call.

Complexity Analysis

Time complexity : O(2^n)
Size of recursion tree will be 2^n

Space complexity : O(n^2)
memo array of size n * n is used.
'''



import sys

def lisMain(num_array):
    '''
    use minint as first prev array
    '''
    minint=-(sys.maxint)-1
    return lis(num_array,minint,0)

def lis(num_array,prev,curr):
    '''
    recursive function to create the LIS
    '''
    print "call made with curr-end: %s-%s" %(curr,len(num_array))
    if curr==len(num_array):
       return 0
    taken=0
    if num_array[curr]>prev:
       taken=1+lis(num_array,num_array[curr],curr+1)
    not_taken=lis(num_array,prev,curr+1)
    return max(taken,not_taken)

if __name__=='__main__':
    print lisMain([10,9,2,5,3,7,101,18])
