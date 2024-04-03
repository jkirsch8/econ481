#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Problem 0


# In[ ]:


def github() -> str:
    """
    Takes no arguments and returns a link to my solutions on Github.
    """

    return "https://github.com/jkirsch8/econ481/blob/main/HW1.py"


# In[ ]:


#Problem 2


# In[14]:


def evens_and_odds(n: int) -> dict:
    """
    Takes an integer argument and prints the sums of all even and odd numbers less than the integer.
    """
    dict = {'evens':0,
           'odds':0}
    for i in range(n):
        if i % 2 == 0:
            dict['evens'] += i
        else:
            dict['odds'] += i
    return dict


# In[17]:


#Problem 3


# In[51]:


from typing import Union

def time_diff(date_1: str, date_2: str, out: str) -> Union[str,float]:
    """
    Takes two dates and returns the number of days in between them as a float or a string if specified.
    """
    from datetime import date,time, datetime, timedelta
    import datetime as dt
    date_1 = datetime.strptime(date_1, '%Y-%m-%d')
    date_2 = datetime.strptime(date_2, '%Y-%m-%d')
    delta = date_1 - date_2
    day_diff = delta.days
    output = day_diff
    if day_diff < 0:
        day_diff = -1*day_diff
    if out == 'string':
        output = f"There are {day_diff} days between two dates"    
    return output


# In[53]:


#Problem 4


# In[56]:


def reverse(in_list: list) -> list:
    """
    Takes in a list as an argument and reverses the order of the list and outputs the reversed list
    """
    outlist = []
    for i in range(len(in_list)-1,-1,-1):
        outlist.append(in_list[i])
    return outlist


# In[59]:


#Problem 5


# In[71]:


def prob_k_heads(n: int, k: int) -> float:
    """
    Takes two integers n and k, and returns the probability of getting k heads out of n coin flips
    """
    n_minus_k_fac = 1
    for i in range(1,n-k+1):
        n_minus_k_fac *= i
    n_choose_k = 1
    for i in range(k+1, n+1):
        n_choose_k *= i
    n_choose_k /= n_minus_k_fac
    prob = n_choose_k / (2**n)
    return prob


# In[72]:


prob_k_heads(2,1)

