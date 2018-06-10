'''
Brute Force Approach
TC: O(sp)
SC: O(s+p)
'''
def subStringBruteForce(s,p):
    #find the required scan end to guard against overflow
    end=len(s)-len(p)+1
    for i in range(0,end):
        found=True
        for j in range(0,len(p)):
            if s[i+j]!=p[j]:
               found=False
               break
        if found:
           return i
    return -1

'''
Homework
KMP Algorithm
'''


if __name__=='__main__':
   print subStringBruteForce("kiran","pan")
   print subStringBruteForce("kiran","iran")
   print subStringBruteForce("kiran","n")
