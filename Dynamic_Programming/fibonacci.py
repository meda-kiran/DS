
'''
Approach: Caching intermediate results
Space: O(n) -> recursion with cache space
Time: liner O(n)
'''
def fibonacci_1(n,cache={}):
    print cache
    if n==0 or n==1:
       cache[n]=n
    elif n not in cache:
       cache[n]=fibonacci_1(n-1)+fibonacci_1(n-2)
    return cache[n]

#print fibonacci_1(10)


'''
Approach: DP
Space: O(1)
Time: Linear O(n)
'''
def fibonacci_2(n):
    if n==0 or n==1:
       return n
    n_minus2=0
    n_minus1=1
    i=2
    while(i<=n):
      tmp=n_minus1
      n_minus1=n_minus1+n_minus2
      n_minus2=tmp
      i+=1
    return n_minus1


for i in range(1,11):
    print "i:%s its fibo:%s" %(i,fibonacci_2(i))
    
