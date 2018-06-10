'''
Example input: "my name is kiran"
Example output: "kiran is name my"
'''

'''
Approach1:
TC: O(n)
SC: O(n)
'''
def reverse_ordering_of_words(s):
    i=len(s)-1
    tmp=''
    revLine=''
    while(i>=0):
        tmp=''
        while(s[i]!=' ' and i>=0):
           tmp=s[i]+tmp
           i=i-1
        revLine=revLine+tmp
        tmp=''
        while(s[i]==' ' and i>=0):
           tmp=s[i]+tmp
           i=i-1
        revLine=revLine+tmp
    return str(revLine)


'''
Approach2
TC: O(n)
SC: O(1)
'''
def _reverse(s,i,j):
    s=list(s)
    left=i
    right=j
    while(left<right):
         tmp=s[left]
         s[left]=s[right]
         s[right]=tmp
         left+=1
         right-=1
    return ''.join(map(str,s))

def reverse_ordering_of_words2(s):
    s=_reverse(s,0,len(s)-1)
    print s
    i=0
    while(i<len(s)):
         startWord=i
         while(i<len(s) and s[i]!=' '):
              i+=1
         s=_reverse(s,startWord,i-1)
         while(i<len(s) and s[i]==' '):
              i+=1
    return s



print reverse_ordering_of_words2("my name is kiran")
