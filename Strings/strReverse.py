def Reverse(s):
    return sReverse(list(s))

def sReverse(s):
    left=0
    right=len(s)-1
    while left<right:
        tmp=s[left]
        s[left]=s[right]
        s[right]=tmp
        left+=1
        right-=1
    return s


if __name__=='__main__':
   print ''.join(Reverse("kiran"))

