def KMP(s,p):
    partial=[0]
    for x in p[1:]:
        prefixIndexTillNow=partial[-1]
        partial.append(prefixIndexTillNow+1 if x==p[prefixIndexTillNow] else 0)
    p_ptr,start,result=0,0,[]
    while((start+len(p)-1)<len(s)):
         while(p_ptr<len(p) and s[start+p_ptr]==p[p_ptr]):
             p_ptr+=1
         if p_ptr==len(p):
            result.append(start)
            start=start+1
         elif p_ptr>0:
              start=start+(p_ptr-partial[p_ptr-1])
         else:
              start=start+1
         p_ptr=0
    result.append(-1)
    return result




print KMP("If you think you think too much, then you might be wrong! Think about it."," you")

#print KMP("CCCCCCCCCC","CC")

#print KMP("abcxabxdabxabcdabcdabcyabcdabcy","abcdabcy")
#print KMP("abcxabxdabxabcdabcdabcyabcdabcyabcdabcyabcdabcyabcdabcy","abcdabcy")

# abcxabxdabxabcdabcdabcyabcdabcy
# abcdabcy

#print KMP("bacbababaabcbab","abababca")
