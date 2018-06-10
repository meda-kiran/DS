def KMP(s,p):
    print s
    print p
    partial=[0]
    for x in p[1:]:
        prefixIndexTillNow=partial[-1]
        partial.append(prefixIndexTillNow+1 if x==p[prefixIndexTillNow] else 0)
    print partial
    
    p_ptr=0
    start=0
    result=[]
    while((start+len(p)-1)<len(s)):
         numMatch=0
         while(p_ptr<len(p) and s[start+p_ptr]==p[p_ptr]):
             print "comparing index %s and %s" %(start+p_ptr,p_ptr)
             print "Comparing %s and %s" %(s[start+p_ptr],p[p_ptr])
             p_ptr+=1
         print "exited comparison"
         if p_ptr==len(p):
            result.append(start)
            start=start+p_ptr
         elif p_ptr>0:
              print "Partial length: %s" %p_ptr
              start=start+(p_ptr-partial[p_ptr-1])
         else:
              start=start+1
         print "now at start: %s" %start
         p_ptr=0
    return result




#print KMP("abcxabxdabxabcdabcdabcyabcdabcy","abcdabcy")
print KMP("abcxabxdabxabcdabcdabcyabcdabcyabcdabcyabcdabcyabcdabcy","abcdabcy")
# abcxabxdabxabcdabcdabcyabcdabcy
# abcdabcy

#print KMP("bacbababaabcbab","abababca")
