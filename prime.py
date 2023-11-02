#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def is_prime(n):
    """
    To check if a number is prime or not.

    Its inputs are integers and outputs are 'True' or 'False' depending on whether the input integer is prime or not respectively. 
    
    Example:
        1) is_prime(7)
        True

        2) is_prime(9)
        False
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# In[ ]:

is_prime(17)

