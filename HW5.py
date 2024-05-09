#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/jkirsch8/econ481/blob/main/HW5.py"


# In[41]:


def scrape_code(url: str) -> str:
    """
    Scrapes code from lecture slides into an executable python script.
    """
    import requests
    from bs4 import BeautifulSoup
    req_obj = requests.get(url)
    soup = BeautifulSoup(req_obj.text)
    code = soup.find_all('code', class_ ='sourceCode python')
    out = ''
    for x in code:
        line = x.text.strip()
        if not line.startswith('%'):
            out += line + '\n'
    
    return out
scrape_code('https://lukashager.netlify.app/econ-481/01_intro_to_python')


# In[38]:


# Scratch Work
import requests
from bs4 import BeautifulSoup
import re
url = 'https://lukashager.netlify.app/econ-481/01_intro_to_python'
req_obj = requests.get(url)
soup = BeautifulSoup(req_obj.text)

#code = soup.find_all('span', id = re.compile('cb.*'))

print(out)
    

    
    








# In[ ]:




