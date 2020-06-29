#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools
import math
import numpy as np
import networkx as nx
import numba
import time
import matplotlib.pyplot as plt


# In[2]:


# Global constants here
f9_4 = {1: 5,
       2: 8,
       6: 18,
       7: 21,
       8: 22,
       9: 25,
       10: 26,
       11: 31,
       12: 32,
       13: 33,
       14: 34,
       15: 31,
       16: 32,
       17: 33}

f10_4 = {1: 15,
        2: 28,
        4: 52,
        5: 63,
        6: 72,
        7: 72,
        8: 72}


# # Utils

# In[ ]:


# @numba.njit()
def choose(n, k):
    '''
    A fast way to calculate binomial coefficients by Andrew Dalke
    '''
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def __integer_partition__(n, k):
    '''
    Returns the partitions of n into exactly k parts
    '''
    def _part(n, k, pre):
        if n <= 0:
            return []
        if k == 1:
            if n <= pre:
                return [[n]]
            return []
        ret = []
        for i in range(min(pre, n), 0, -1):
            ret += [[i] + sub for sub in _part(n-i, k-1, i)]
        return ret
    return _part(n, k, n)



def composed_of(arr1, arr2):
    '''
    Returns True if and only if None of arr1 elements are in arr2 else returns false
    '''
    for elem in arr1:
        if elem in arr2:
            return False
    return True


# # Kneser Related

# In[32]:


def kneser_girth(n, k):
    '''
     Returns the girth of the Kneser graph
    '''
    g = 6 if n == 2*k + 1 else 4
    expr = 2 * np.ceil(k / (n - 2*k)) + 1
    return int(np.minimum(g, expr))



def U(n, k, c, S):
    '''
    Upper Bound on crossing edges e(S\K(n, k)) obtained from the Laplacian Eigenvalues
    '''
    deg = choose(n - k, k)
    vertices = choose(n, k)
    last_laplacian_eval = (deg + choose(n - k - 1, k - 1))    
    return int(np.minimum(deg*S, np.floor((last_laplacian_eval * S * (vertices - S)) / (vertices))))



def a(n, k, c, S):
    '''
    Lower bound on the possible number of singletons in c components
    '''
    deg = choose(n - k, k)
    return int(np.ceil((-2*c + 2*c*deg - U(n, k, c, S)) / (deg - 2)))



def f(n, k, S):
    '''
    Piecewise (increasing) function which provides a lower bound on the number of edges
    from a single component to S
    '''
    deg = choose(n - k, k)
    vertices = choose(n, k)
    second_laplacian_eval = deg - np.power(-1,2%2) * choose(n - k - 2, k - 2)
    if(n == 10 and k == 4):
        if(f10_4.get(S) == None):
            if(S >= 96):
                return 470
        else:
            return f10_4.get(S)
    if(n == 9 and k == 4 and f9_4.get(S) != None):
        return f9_4.get(S)    
    return int(np.minimum(deg*S, np.ceil(second_laplacian_eval * S * (vertices - S)/(vertices))))



def l(n, k, part):
    '''
    Sums up all the possible lower bounds for edges for each component in the partition list
    '''
    return np.sum(np.vectorize(f)(n,k,part))



def P(n, k, c):
    S = int(np.ceil((n/k - 1) * c) - 1)
    deg = choose(n - k, k)
    comps = a(n,k,c,S)
    vertices = choose(n, k)
    girth = kneser_girth(n, k) 
    lim = U(n,k,c,S) - int(deg * comps)
    
    print('n = %d, k = %d, c = %d, S = %d, a = %d, vertices = %d, degree = %d, limit = %d'%(n,k,c,S,comps,vertices,deg,lim))    
    print('Partition %d, into exactly %d parts'%(int(vertices - S - comps), int(c - comps)))
    partition_lst = __integer_partition__(int(vertices - S - comps), int(c - comps))
    
    lst = []
    for i in range(len(partition_lst)):
        lval = l(n,k,partition_lst[i])
        if(lval <= lim and (len(partition_lst[i]) <= int(c - comps)) and composed_of(list(range(3, girth)),partition_lst[i])==True):
            lst.append(partition_lst[i])
    print('Selected %d out of %d total partitions\n'%(len(lst), len(partition_lst)))
    print(*lst, sep='\n')


# In[33]:


P(10,4,74)
# 424

# l(10,4,[23, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])


# ### K(10,4) for 57 $\leq$ c $\leq$ 75

# In[35]:


for i in range(57,75 + 1):
    print('*'*50,i,'*'*50)
    start = time.time()
    P(10,4,i)
    end = time.time()
    print('Time = %.5f seconds'%(end-start))


# ### K(9,4) for 41 $\leq$ c $\leq$ 53

# In[ ]:


for i in range(41,53 + 1):
    print('*'*50,i,'*'*50)
    start = time.time()
    P(9,4,i)
    end = time.time()
    print('Time = %.5f seconds'%(end-start))


# In[ ]:




