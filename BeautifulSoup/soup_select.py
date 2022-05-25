#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[7]:


base_url = 'https://tw.hjwzw.com'
uri = '/Book/Chapter/2244'
res = requests.get(base_url + uri)


# In[9]:


soup = BeautifulSoup(res.text, 'lxml')


# In[11]:


for i in soup.select("#tbchapterlist a"):
    print(base_url + i['href'], i.text)

